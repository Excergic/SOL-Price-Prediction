from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

def export_mongo_to_csv(mongo_uri=MONGODB_URL, db_name="crypto_db", collection_name="sol_price", csv_file="sol_price.csv"):
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Fetch all records from the collection
    cursor = collection.find()

    # Convert the records to a DataFrame
    df = pd.DataFrame(list(cursor))

    # drop the mongoDB _id field
    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)
    
    # export the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Exported {len(df)} records to CSV file '{csv_file}'.")

if __name__ == "__main__":
    print("Exporting data from MongoDB to CSV...")
    export_mongo_to_csv()
    print("Done.")  
    