from pyspark.sql import SparkSession
from pyspark.sql.functions import hour, col, avg, count, sum, when

def start_spark():
    return SparkSession.builder.appName("RefinedKPIs").getOrCreate()

def main():
    spark = start_spark()

    print("Cargando datos limpios...")
    df = spark.read.parquet("data/cleaned_2024.parquet")

    print("Calculando KPIs...")

    trips_per_hour = (
        df.withColumn("pickup_hour", hour("tpep_pickup_datetime"))
          .groupBy("pickup_hour")
          .agg(count("*").alias("trips"))
          .orderBy("pickup_hour")
    )

    avg_income_per_trip = df.select(avg("total_amount").alias("avg_total_income"))

    avg_distance_by_zone = (
        df.groupBy("PULocationID")
          .agg(avg("trip_distance").alias("avg_distance"))
          .orderBy("PULocationID")
    )

    payment_distribution = (
        df.withColumn("cash", when(col("payment_type") == 2, 1).otherwise(0))
          .withColumn("card", when(col("payment_type") == 1, 1).otherwise(0))
          .agg(
              (sum("cash") / count("*") * 100).alias("cash_percentage"),
              (sum("card") / count("*") * 100).alias("card_percentage")
          )
    )

    avg_tip_by_payment = (
        df.groupBy("payment_type")
          .agg(avg("tip_amount").alias("avg_tip"))
          .orderBy("payment_type")
    )

    total_income_by_zone = (
        df.groupBy("PULocationID")
          .agg(sum("total_amount").alias("total_income"))
          .orderBy("total_income", ascending=False)
    )

    avg_passengers = df.select(avg("passenger_count").alias("avg_passenger_count"))

    print("Guardando resultados...")

    trips_per_hour.write.mode("overwrite").parquet("REFINED/kpi_trips_per_hour.parquet")
    avg_income_per_trip.write.mode("overwrite").parquet("REFINED/kpi_avg_income.parquet")
    avg_distance_by_zone.write.mode("overwrite").parquet("REFINED/kpi_avg_distance_by_zone.parquet")
    payment_distribution.write.mode("overwrite").parquet("REFINED/kpi_payment_distribution.parquet")
    avg_tip_by_payment.write.mode("overwrite").parquet("REFINED/kpi_avg_tip_by_payment.parquet")
    total_income_by_zone.write.mode("overwrite").parquet("REFINED/kpi_total_income_by_zone.parquet")
    avg_passengers.write.mode("overwrite").parquet("REFINED/kpi_avg_passenger_count.parquet")

    print("KPIs calculados y almacenados correctamente.")

if __name__ == "__main__":
    main()
