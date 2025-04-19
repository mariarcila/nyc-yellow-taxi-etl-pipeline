from pyspark.sql import SparkSession
import os

def start_spark(app_name: str = "RawLayer"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def get_parquet_paths(folder_path: str, year: str):
    files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.startswith(f"yellow_tripdata_{year}-") and f.endswith(".parquet")
    ]
    return files

def main():
    spark = start_spark()
    folder_path = "data"
    year = "2024"

    parquet_files = get_parquet_paths(folder_path, year)
    df = spark.read.parquet(*parquet_files)

    df.show(5)
    print(f"Total records loaded for {year}: {df.count()}")

if __name__ == "__main__":
    main()
