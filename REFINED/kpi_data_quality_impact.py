from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit

def main():
    print("Cargando datos limpios...")
    spark = SparkSession.builder.appName("Data Quality Impact KPIs").getOrCreate()

    cleaned_path = "data/cleaned_2024.parquet"
    df_cleaned = spark.read.parquet(cleaned_path)

    total_records_raw = 3000000
    valid_records = df_cleaned.count()
    discarded_records = total_records_raw - valid_records
    discard_rate = discarded_records / total_records_raw

    print("Calculando KPIs de calidad de datos...")

    null_stats = df_cleaned.select([
        (count(when(col(c).isNull(), c)) / valid_records).alias(f"{c}_null_pct")
        for c in ["passenger_count", "trip_distance", "fare_amount"]
    ])

    kpi_df = null_stats.withColumn("valid_records", lit(valid_records)) \
                       .withColumn("discarded_records", lit(discarded_records)) \
                       .withColumn("discard_rate", lit(discard_rate))

    output_path = "data/kpis/kpi_data_quality_impact.parquet"
    kpi_df.write.mode("overwrite").parquet(output_path)

    print(f"KPIs guardados en: {output_path}")

if __name__ == "__main__":
    main()