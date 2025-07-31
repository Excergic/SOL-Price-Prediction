# ETL Pipeline for MLOps Project

## Description

This is a simple ETL pipeline for the MLOps project. I have not build end to end ml pipeline, but this is a simple ETL pipeline that I have built to get the data from the source and load it into the target (NoSQL DB).

## Clone the repository
```bash
git clone https://github.com/Excergic/SOL-Price-Prediction.git
cd SOL-Price-Prediction
```

## Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## MongoDB Connection

Create a `.env` file in the root directory

```bash
cp .env.example .env
```
Above command will create a `.env` file with the following content

```bash
MONGODB_URL=YOUR_MONGODB_URL
```
## How to get MongoDB URL

## 1. Goto this link 
```bash
https://www.mongodb.com/products/platform/atlas-database
```

## 2. Create a free account with M0 free tier
![Cluster](https://raw.githubusercontent.com/Excergic/images/main/cluster0.png)

## 3. Set Driver
![Drivers](https://raw.github.com/Excergic/images/main/driver2.png)

## 4. Get the connection string
![Connection](https://raw.githubusercontent.com/Excergic/images/main/connection3.png)

### 5. Copy the connection string and paste it in the .env file

## 6. Set Password (if not set) follow these steps:
![Password](https://raw.github.com/Excergic/images/main/password7.png)
![Password](https://raw.github.com/Excergic/images/main/password8.png)
![Password](https://raw.githubusercontent.com/Excergic/images/main/password9.png)
![Password](https://raw.github.com/Excergic/images/main/password10.png)
![Password](https://raw.githubusercontent.com/Excergic/images/main/final11.png)


### - After copying the password, replace the password in connection string with the new password, make sure you remove `<>` as well. 


## 7. Set Network

![Network](https://raw.githubusercontent.com/Excergic/images/main/network4.png)
![Network](https://raw.githubusercontent.com/Excergic/images/main/network5.png)
![Add Network](https://raw.githubusercontent.com/Excergic/images/main/addnetwork6.png)

## 8. You are good to go.

```bash
# Run the script /etl/push_data.py
# This will extract the data from coingecko API, trasnfrom and load it into MongoDB
python push_data.py

# Run the script /etl/get_data_from_db.py
# This will export the data from MongoDB to CSV file
python get_data_from_db.py  

``` 

## Contact 

Twitter: [@dhaivat00](https://x.com/dhaivat00)  
LinkedIn: [Dhaivat Jambudia](https://www.linkedin.com/in/dhaivat-jambudia/)
