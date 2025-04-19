# NYC Yellow Taxi ETL Pipeline

Este repositorio contiene un pipeline ETL construido con PySpark, basado en el procesamiento de datos públicos sobre los viajes realizados por taxis amarillos en la ciudad de Nueva York. El proyecto sigue una arquitectura de medallón que organiza los datos en tres capas: Raw, Trusted y Refined.

## Objetivo

Transformar datos en crudo en información útil para el análisis, mediante un proceso estructurado que incluye validación, enriquecimiento geográfico y generación de indicadores clave. Este proyecto forma parte de una prueba técnica para una vacante de ingeniería de datos.

## Arquitectura

El pipeline se divide en tres capas:

- **Raw Layer**: Lectura y almacenamiento de los datos originales obtenidos desde un bucket público en AWS S3, sin modificaciones.
- **Trusted Layer**: Limpieza y validación de datos; se filtran registros erróneos, se corrigen outliers y se unen datos con información geográfica extraída de la Taxi Zone Lookup.
- **Refined Layer**: Agregaciones y generación de KPIs para el análisis. Aquí se calculan métricas como la demanda por franja horaria, eficiencia operativa por zona, y se evalúa el impacto de la calidad de los datos.

## Tecnologías utilizadas

- Python 3.13
- Apache Spark (PySpark)
- AWS S3 (Open Data)
- Git y GitHub

## Estructura del proyecto

```
nyc-yellow-taxi-etl-pipeline/
├── raw/              # Scripts de extracción de datos
├── trusted/          # Limpieza, validación y enriquecimiento
├── refined/          # Agregaciones y KPIs
├── utils/            # Funciones auxiliares (logs, validaciones)
├── config/           # Archivos de configuración
├── requirements.txt  # Dependencias del proyecto
├── execution_report.json  # Reporte generado automáticamente del proceso ETL
└── README.md         # Documentación general del proyecto
```
