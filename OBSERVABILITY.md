# Observability Layer

This module ensures quality control and monitoring of the data cleaning process applied to NYC yellow taxi trips. It is part of the Trusted Layer and allows us to track the performance and results of the ETL pipeline.

## Purpose

The goal of the observability layer is to provide transparency into what happened during data cleaning — how many records were processed, how many were discarded or validated, and how long it took. This is essential to trust the data used in the Refined Layer.

## Script: `observability_metrics.py`

This script performs the following actions:

- Loads the cleaned data from `data/cleaned_2024.parquet`.
- Validates the data types and essential columns again.
- Measures the number of:
  - Total records processed.
  - Valid records (that meet business rules).
  - Discarded records.
- Logs:
  - Start and end timestamps.
  - Total execution time (in seconds).

## Output

A single `.json` report with the following structure is generated and stored at:

```
data/observability_report.json
```

Sample content:

```json
{
  "start_time": "2024-04-19T11:34:52",
  "end_time": "2024-04-19T11:34:59",
  "execution_time_seconds": 7,
  "total_records": 2872671,
  "valid_records": 2869714,
  "discarded_records": 2957
}
```

## Importance

Including this layer helps ensure:
- **Transparency**: Knowing what was cleaned and how much was affected.
- **Reproducibility**: Same inputs and rules should yield the same observability output.
- **Traceability**: Clear logs and outputs help identify problems early in the pipeline.

## Status

Script executed successfully  
Report stored and committed  
No performance issues detected
