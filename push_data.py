import requests
from datetime import datetime
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL") 

def fetch_sol_historical(days=120):
    url = "https://api.coingecko.com/api/v3/coins/solana/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days  # 120 days (~4 months)
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Extract prices and volumes
    prices = data.get('prices', [])
    volumes = data.get('total_volumes', [])

    # Create DataFrames from lists
    df_prices = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df_volumes = pd.DataFrame(volumes, columns=['timestamp', 'volume'])

    # Merge on timestamp
    df = pd.merge(df_prices, df_volumes, on='timestamp')

    # Convert timestamp from ms to datetime object (UTC)
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Reorder columns and drop the original timestamp
    df = df[['datetime', 'price', 'volume']]

    return df

def load_data_to_mongodb(df, mongo_uri=MONGODB_URL, db_name="crypto_db", collection_name="sol_price"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Convert DataFrame rows to dict and insert into MongoDB
    records = df.to_dict(orient='records')

    # Optional: clear collection before inserting new data (comment if not wanted)
    collection.delete_many({})

    result = collection.insert_many(records)
    print(f"Inserted {len(result.inserted_ids)} records into MongoDB collection '{collection_name}'.")

if __name__ == "__main__":
    print("Fetching historical data for Solana...")
    df_sol = fetch_sol_historical(days=90)
    print(f"Fetched {len(df_sol)} records.")

    print("Loading data into MongoDB...")
    load_data_to_mongodb(df_sol)

    print("Done.")