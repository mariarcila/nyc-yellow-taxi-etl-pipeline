# NYC yellow taxi ETL pipeline

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


## Trusted Layer

Esta capa contiene los datos crudos procesados y limpiados. El script `clean_trusted.py` realiza las siguientes acciones:

- Carga los datos `.parquet` desde la carpeta `RAW`.
- Aplica filtros para eliminar registros inválidos o incompletos.
- Verifica que los tipos de datos sean correctos.
- Guarda los datos limpios en `data/cleaned_2024.parquet`.

Total de registros limpios: **2.869.714**



## Refined Layer

En esta capa se realiza el análisis y la generación de indicadores clave (KPIs) para facilitar la toma de decisiones basada en datos. A partir de los datos limpios de la capa Trusted, se llevan a cabo agregaciones temporales, espaciales y económicas que permiten sintetizar la operación de los taxis amarillos en Nueva York durante el año 2024.

El script `generate_kpis.py` realiza las siguientes tareas:

- Carga los datos validados desde `data/cleaned_2024.parquet`.
- Calcula métricas agregadas por hora, por zona y por tipo de pago.
- Genera un archivo `refined_kpis.csv` que contiene los KPIs extraídos.

### Principales KPIs generados

- Total de viajes por zona de recogida.
- Ingreso promedio por viaje (por zona y por hora).
- Distancia media recorrida.
- Distribución de métodos de pago.
- Total recaudado por franja horaria.
- Propina media y su relación con el total pagado.
- Cantidad de pasajeros transportados por hora y por zona.
- Relación entre duración del viaje y monto pagado.

Este archivo se encuentra en la ruta `REFINED/refined_kpis.csv` y puede ser utilizado en herramientas de visualización o análisis adicional.

