from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, col, count

def main():
    print("Cargando datos limpios...")

    spark = SparkSession.builder \
        .appName("KPIs Demand and Peak Hours") \
        .getOrCreate()

    spark.conf.set("spark.sql.shuffle.partitions", "1")

    input_path = "data/cleaned_2024.parquet"
    output_path = "data/kpis/kpi_demand_peak_hours.parquet"

    df = spark.read.parquet(input_path)

    print("Calculando KPIs de demanda y tiempos pico...")

    demand_by_hour = df.withColumn("pickup_hour", hour(col("tpep_pickup_datetime"))) \
        .groupBy("pickup_hour") \
        .agg(count("*").alias("trips_count")) \
        .orderBy("pickup_hour")

    result_df = demand_by_hour

    result_df.write.mode("overwrite").parquet(output_path)

    print("KPIs guardados en:", output_path)

    spark.stop()

if __name__ == "__main__":
    main()
