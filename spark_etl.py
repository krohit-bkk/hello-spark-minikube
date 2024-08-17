# spark_etl.py

from pyspark.sql import SparkSession
import time

def etl():
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("Dummy ETL Process") \
        .getOrCreate()

    # Create a dummy DataFrame
    data = [("Alice", 30), ("Bob", 28), ("Cathy", 25)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)

    # Print the DataFrame
    df.show()
    time.sleep(60)

    df.write.format("csv").mode("overwrite").save("/minikube-host/output1/")

    # Stop the Spark session
    spark.stop()

def main():
    etl()

if __name__ == "__main__":
    main()
