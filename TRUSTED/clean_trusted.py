from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def start_spark(app_name="TrustedDataCleaning"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def load_raw_data(spark, path):
    return spark.read.parquet(path)

def clean_data(df):
    # Elimina filas con valores nulos en columnas críticas
    cleaned_df = df.dropna(subset=[
        "VendorID", 
        "tpep_pickup_datetime", 
        "tpep_dropoff_datetime", 
        "PULocationID", 
        "DOLocationID", 
        "fare_amount"
    ])

    # Filtra viajes con distancias negativas o nulas
    cleaned_df = cleaned_df.filter(col("trip_distance") > 0)

    # Filtra tarifas negativas o nulas
    cleaned_df = cleaned_df.filter(col("fare_amount") > 0)

    return cleaned_df

def main():
    spark = start_spark()
    
    input_path = "data/yellow_tripdata_2024-01.parquet"
    output_path = "data/cleaned_2024.parquet"

    print("Cargando datos crudos...")
    df_raw = load_raw_data(spark, input_path)

    print("Aplicando limpieza básica...")
    df_cleaned = clean_data(df_raw)

    df_cleaned.show(5)
    print(f"Total de registros limpios: {df_cleaned.count()}")

    df_cleaned.write.mode("overwrite").parquet(output_path)
    print(f"Datos limpios guardados en {output_path}")

if __name__ == "__main__":
    main()