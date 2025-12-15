# X (Twitter) ETL Pipeline with Airflow on AWS EC2

##  Project Overview
This project implements a simple **ETL (Extract, Transform, Load)** pipeline using **X (Twitter) API v2**.  
The pipeline is orchestrated using **Apache Airflow**, deployed on an **AWS EC2** instance, and stores the processed data in **Amazon S3**.

The workflow consists of **a single Airflow DAG** with one task that extracts tweet data from a specific X (Twitter) user, transforms it into a structured format, and loads it into S3 as a CSV file.

---

## Architecture
![ss](ss.png)
1. **Extract**
   - Fetches tweets using **Tweepy** and **X API v2**
   - Retrieves tweet content, engagement metrics, and timestamps

2. **Transform**
   - Cleans and structures the raw API response
   - Converts data into a Pandas DataFrame

3. **Load**
   - Saves transformed data as a CSV file
   - Uploads directly to **Amazon S3** using `s3fs`

4. **Orchestration**
   - Managed by **Apache Airflow**
   - Executed on **AWS EC2**

---

##  Tech Stack
- **Programming Language**: Python
- **API**: X (Twitter) API v2
- **Orchestration**: Apache Airflow
- **Cloud Platform**: AWS EC2
- **Storage**: Amazon S3
- **Libraries**:
  - tweepy
  - pandas
  - python-dotenv
  - s3fs

---

##  ETL Process
The ETL logic is implemented in the `run_etl()` function:
- Authenticates to X API using credentials from a `.env` file
- Fetches the latest 10 tweets from a specific username
- Extracts relevant fields:
  - Username
  - Tweet text
  - Like count
  - Retweet count
  - Tweet creation timestamp
- Stores the processed data as a CSV file in Amazon S3

---

##  Airflow DAG
- **DAG Name**: `twitter_etl_dag`
- **Description**: Simple Twitter ETL DAG
- **Start Date**: January 1, 2024
- **Schedule**: Manual (no schedule interval defined)
- **Retries**: 1 retry with 1-minute delay

### Tasks
- `run_twitter_etl`  
  Executes the ETL process using a `PythonOperator`.

---

##  Environment Variables (.env)
This project uses a `.env` file to store sensitive credentials securely.

### Example `.env` File
```env
# X (Twitter) API Credentials
BEARER_TOKEN=your_x_api_bearer_token
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret

# AWS Credentials
AWS_ACCESS_KEY=your_aws_access_key_id
AWS_SECRET_KEY=your_aws_secret_access_key
