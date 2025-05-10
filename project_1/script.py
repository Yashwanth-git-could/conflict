from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, trim, lower, initcap
from pyspark.sql.types import DoubleType
 
# Initialize Spark session
spark = SparkSession.builder.appName("CleanAndMergeTransactions").getOrCreate()
 
# Read all CSV files from the dirty data folder
df = spark.read.option("header", True).csv("gs://yashwbank-bucket/transactions/*.csv")
# Clean and standardize columns
 
# 1. Status: trim, lowercase, and validate
df = df.withColumn("Status", trim(lower(col("Status"))))
df = df.withColumn("Status", when(col("Status").isin("success", "failed", "pending"), col("Status")).otherwise(None))
 
# 2. Payment_Method: trim, lowercase, and validate
df = df.withColumn("Payment_Method", trim(lower(col("Payment_Method"))))
valid_methods = ["credit card", "debit card", "upi", "net banking", "cash"]
df = df.withColumn("Payment_Method", when(col("Payment_Method").isin(valid_methods), col("Payment_Method")).otherwise(None))
 
# 3. Product_Category: trim, lowercase, and validate
df = df.withColumn("Product_Category", trim(lower(col("Product_Category"))))
valid_categories = ["electronics", "clothing", "groceries", "home decor", "toys", "books"]
df = df.withColumn("Product_Category", when(col("Product_Category").isin(valid_categories), col("Product_Category")).otherwise(None))
 
# 4. Amount: cast to double and validate range
df = df.withColumn("Amount", col("Amount").cast(DoubleType()))
df = df.withColumn("Amount", when(col("Amount") < 0, None).otherwise(col("Amount")))
 
# 5. Branch_ID: validate format (e.g., "MUM-AND")
df = df.withColumn("Branch_ID", when(col("Branch_ID").rlike("^[A-Z]{3}-[A-Z]{3}$"), col("Branch_ID")).otherwise(None))
 
# 6. Format City and Branch_Name
df = df.withColumn("City", initcap(col("City")))
df = df.withColumn("Branch_Name", initcap(col("Branch_Name")))
 
# 7. Remove rows with null or blank Transaction_ID or Customer_ID
df = df.filter((trim(col("Transaction_ID")) != "") & col("Transaction_ID").isNotNull())
df = df.filter((trim(col("Customer_ID")) != "") & col("Customer_ID").isNotNull())
 
# 8. Remove rows with any null or blank values in any column
for c in df.columns:
    df = df.filter((col(c).isNotNull()) & (trim(col(c)) != ""))
 
# 9. Drop duplicates
df = df.dropDuplicates()
 
# 10. Write cleaned and merged data to a single file
df.coalesce(1).write.mode("overwrite").option("header", True).csv("gs://yashwbank-bucket/cleaned/merged_transactions.csv")

