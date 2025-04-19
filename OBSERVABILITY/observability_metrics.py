from datetime import datetime
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder.appName("ObservabilityMetrics").getOrCreate()

    input_path = "data/cleaned_2024.parquet"
    output_path = "data/observability_report.json"

    start_time = datetime.now()

    print("Cargando datos limpios...")
    df = spark.read.parquet(input_path)

    total_records = df.count()

    df_valid = df.filter(
        (col("passenger_count") > 0) &
        (col("trip_distance") > 0) &
        (col("fare_amount") >= 0) &
        (col("total_amount") >= 0)
    )

    valid_records = df_valid.count()
    discarded_records = total_records - valid_records

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    report = {
        "layer": "Trusted",
        "start_time": str(start_time),
        "end_time": str(end_time),
        "execution_time_seconds": duration,
        "total_records": total_records,
        "valid_records": valid_records,
        "discarded_records": discarded_records
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print("Informe de observabilidad generado correctamente.")
    spark.stop()

if __name__ == "__main__":
    main()
