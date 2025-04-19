from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, sum as spark_sum

def main():
    print("Cargando datos limpios...")
    spark = SparkSession.builder.appName("GeoEconomicKPIs").getOrCreate()

    input_path = "data/cleaned_2024.parquet"
    output_path = "data/kpis/kpi_geoeconomic_efficiency.parquet"

    df = spark.read.parquet(input_path)
    print("Calculando KPIs de eficiencia geográfica y económica...")

    revenue_by_zone = (
        df.groupBy("DOLocationID")
        .agg(
            spark_sum("total_amount").alias("total_revenue"),
            count("*").alias("total_trips")
        )
        .withColumn("avg_revenue_per_trip", col("total_revenue") / col("total_trips"))
    )

    base_fare_by_pickup = (
        df.groupBy("PULocationID")
        .agg(
            avg("fare_amount").alias("avg_fare_amount"),
            count("*").alias("num_trips")
        )
    )

    pickup_density = (
        df.groupBy("PULocationID")
        .count()
        .withColumnRenamed("count", "pickup_count")
    )

    result_df = base_fare_by_pickup.join(
        pickup_density, on="PULocationID", how="left"
    )

    result_df = result_df.join(
        revenue_by_zone.withColumnRenamed("DOLocationID", "PULocationID"),
        on="PULocationID",
        how="left"
    )

    result_df.write.mode("overwrite").parquet(output_path)
    print(f"KPIs guardados en: {output_path}")

if __name__ == "__main__":
    main()