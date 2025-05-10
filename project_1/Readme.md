

# Title: Failed Transactions Pipeline using GCP (PySpark, Cloud SQL, BigQuery)

## 🔍 Project Overview

This project demonstrates a complete data engineering pipeline built on **Google Cloud Platform (GCP)** using the following components:

- **Google Cloud Storage (GCS)** to store input data and scripts
- **Dataproc** for distributed PySpark processing
- **Cloud SQL (MySQL)** for structured storage
- **BigQuery** for final querying and reporting

We focus on extracting and cleaning banking transaction data, filtering failed transactions, and storing them in BigQuery for reporting.

---

## ☁️ Step 1: Create GCS Bucket

```bash
gsutil mb gs://yashwbank-bucket/
````

---

## 📂 Step 2: Upload Data and Scripts to GCS

```bash
# Upload CSVs
gsutil cp "C:\Users\yashw\OneDrive\Documents\Desktop\rev pro\project_1\transaction_data_dirty\*.csv" gs://yashwbank-bucket/transactions/

# Upload PySpark script
gsutil cp "C:\Users\yashw\OneDrive\Documents\Desktop\rev pro\project_1\script.py" gs://yashwbank-bucket/script1/
```

---

## 🛠️ Step 3: Create Dataproc Cluster

```bash
gcloud dataproc clusters create bank-cluster \
  --region=us-central1 \
  --zone=us-central1-a \
  --single-node \
  --master-machine-type=n1-standard-2 \
  --image-version=2.0-debian10
```

---

## 🚀 Step 4: Submit PySpark Job

```bash
gcloud dataproc jobs submit pyspark gs://yashwbank-bucket/script1/script.py \
  --cluster=bank-cluster \
  --region=us-central1
```

---

## 🧾 Step 5: Create Table in Cloud SQL

```sql
CREATE TABLE failed_transactions (
    Transaction_ID VARCHAR(50),
    Customer_ID VARCHAR(50),
    Amount DOUBLE,
    Date VARCHAR(20),
    Status VARCHAR(20),
    Branch_ID VARCHAR(20),
    Branch_Name VARCHAR(50),
    City VARCHAR(50),
    Payment_Method VARCHAR(30),
    Merchant_Name VARCHAR(100),
    Product_Category VARCHAR(50)
);
```

---

## 🧪 Step 6: Write Failed Records to MySQL in PySpark

> Update your PySpark script with the following:

```python
filtered_df = df.filter(col("Status") == "failed")

filtered_df.write \
  .format("jdbc") \
  .option("url", "jdbc:mysql://<PUBLIC_IP>:3306/<DB_NAME>") \
  .option("driver", "com.mysql.cj.jdbc.Driver") \
  .option("dbtable", "failed_transactions") \
  .option("user", "mysql") \
  .option("password", "Yashwanth@7") \
  .mode("append") \
  .save()
```

---

## 📊 Step 7: Load into BigQuery via EXTERNAL\_QUERY

```sql
CREATE OR REPLACE TABLE `yashwanth-312.BankingDS.failed_transactions` AS
SELECT *
FROM EXTERNAL_QUERY(
  "yashwanth-312.us.tsql",
  "SELECT * FROM failed_transactions WHERE Status = 'failed';"
);
```

---

## ✅ Pipeline Summary

| Component | Description                            |
| --------- | -------------------------------------- |
| GCS       | Raw data and PySpark script storage    |
| Dataproc  | Cleans, transforms, and filters data   |
| Cloud SQL | Stores failed transactions             |
| BigQuery  | Provides analytics and reporting layer |

---

## 📌 Notes

* Ensure JDBC JAR is available in the script's `--jars` parameter
* Cloud SQL must be publicly accessible or tunneled for Dataproc
* EXTERNAL\_QUERY uses a defined connection in BigQuery (e.g., `us.tsql`)
