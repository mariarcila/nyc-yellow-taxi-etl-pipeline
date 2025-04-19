# Pipeline Architecture

This project implements a medallion-style ETL architecture using PySpark to process NYC Yellow Taxi data. The pipeline is structured in four layers, each one with a specific purpose:

## 1. Raw Layer
- **Purpose**: Store the original data without any transformation.
- **Process**: Loads the 12 monthly Parquet files from NYC Open Data into a local folder.
- **Output**: Raw data is stored in `data/raw/`.

## 2. Trusted Layer
- **Purpose**: Clean and validate the raw data.
- **Process**: Applies filters to remove invalid rows (e.g., negative fares, zero distance), fixes column types, and enriches the dataset with zone lookup information.
- **Output**: Clean data saved as `data/cleaned_2024.parquet`.

## 3. Observability Layer
- **Purpose**: Track the quality and performance of the cleaning process.
- **Process**: Logs the total number of records, valid/invalid counts, and execution time.
- **Output**: A JSON report stored at `data/observability_report.json`.

## 4. Refined Layer
- **Purpose**: Generate KPIs for analysis and decision-making.
- **Process**: Calculates aggregated metrics across three dimensions:
  - **Demand & Peak Hours**
  - **Geoeconomic Efficiency**
  - **Data Quality Impact**
- **Output**: Each group of KPIs is saved as a Parquet file in `data/kpis/`.

