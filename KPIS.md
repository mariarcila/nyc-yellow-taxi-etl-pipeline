# Key Performance Indicators (KPIs) – Refined Layer

This document describes the KPIs generated in the **Refined Layer** of the NYC Yellow Taxi ETL pipeline. These indicators are the result of analytical transformations applied to the cleaned dataset and are intended to extract relevant insights for understanding the operational and economic behavior of the taxi system in New York City during 2024.

All KPIs are stored in `.parquet` format under the `data/kpis/` directory.

---

##  Objective

The KPIs aim to:

- Quantify and analyze **taxi demand patterns** across time and locations.
- Evaluate **economic performance and operational efficiency**.
- Assess how **data quality issues** may affect the analysis or lead to biased interpretations.

---

##  Structure of KPI Blocks

The KPIs are grouped into the following three blocks, each calculated by a dedicated script:

1. [Demand and Peak Hours](#1-demand-and-peak-hours)
2. [Geographic and Economic Efficiency](#2-geographic-and-economic-efficiency)
3. [Data Quality Impact](#3-data-quality-impact)

---

## 1. Demand and Peak Hours

**Script:** `REFINED/kpi_demand_peak_hours.py`  
**Output:** `data/kpis/kpi_demand_peak_hours.parquet`

### KPIs calculated:

- **Total trips per hour**  
  Calculates the number of trips started in each hour of the day to detect demand peaks.

- **Total trips per day**  
  Aggregates the number of trips by date to analyze daily demand fluctuations.

- **Top 5 peak hours**  
  Identifies the hours with the highest average demand across all days.

- **Top 5 high-demand days**  
  Detects specific dates with unusually high taxi activity.

### Why it's useful:
These indicators help to understand when the demand for taxis is highest, which can support resource allocation, fleet distribution, and pricing strategies.

---

## 2. Geographic and Economic Efficiency

**Script:** `REFINED/kpi_geoeconomic_efficiency.py`  
**Output:** `data/kpis/kpi_geoeconomic_efficiency.parquet`

### KPIs calculated:

- **Average fare per trip by pickup zone**  
  Measures revenue generation in each pickup area.

- **Average distance per trip by pickup zone**  
  Helps evaluate whether zones with higher fares also have longer trips or if short trips are overcharged.

- **Average tip percentage by payment type**  
  Indicates client satisfaction patterns and potential tipping behavior across different payment methods.

- **Revenue per mile ratio**  
  Estimates operational efficiency by comparing total fare amounts to distance traveled.

### Why it's useful:
These KPIs combine spatial and economic factors to highlight which areas are more profitable or efficient, providing insights for drivers, operators, or regulatory entities.

---

## 3. Data Quality Impact

**Script:** `REFINED/kpi_data_quality_impact.py`  
**Output:** `data/kpis/kpi_data_quality_impact.parquet`

### KPIs calculated:

- **Number of missing or null values per column**  
  Identifies data fields with the most integrity issues.

- **Share of invalid records discarded during cleaning**  
  Calculates the percentage of original data that was removed due to validation rules.

- **Potential revenue loss from discarded records**  
  Estimates how much income (from fares) may have been excluded due to poor data quality.

### Why it's useful:
These indicators quantify the extent to which data quality affects analysis results and decision-making. They highlight risks associated with incomplete or incorrect records.

---

##  Summary

| KPI Block                    | Output File                                        | Purpose                                                  |
|-----------------------------|----------------------------------------------------|----------------------------------------------------------|
| Demand & Peak Hours         | `kpi_demand_peak_hours.parquet`                   | Understand demand patterns over time                     |
| Geo-Economic Efficiency     | `kpi_geoeconomic_efficiency.parquet`              | Assess profitability by zone and payment behavior        |
| Data Quality Impact         | `kpi_data_quality_impact.parquet`                 | Quantify how missing or invalid data affects results     |

---

##  Output Directory Structure

```
data/
└── kpis/
    ├── kpi_demand_peak_hours.parquet
    ├── kpi_geoeconomic_efficiency.parquet
    └── kpi_data_quality_impact.parquet
```

---

##  Next Steps

Make sure each of these `.parquet` files has been committed and pushed to your GitHub repository. They are essential deliverables for this technical challenge and demonstrate your ability to go beyond basic ETL by implementing insightful data analytics.

