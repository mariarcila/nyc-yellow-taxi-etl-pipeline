# NYC Yellow Taxi ETL Pipeline

Este repositorio contiene un pipeline ETL construido con PySpark, basado en el procesamiento de datos públicos sobre los viajes realizados por taxis amarillos en la ciudad de Nueva York. El proyecto sigue una arquitectura de medallón que organiza los datos en tres capas: Raw, Trusted y Refined, e incluye una capa adicional de observabilidad.

## Objetivo

Transformar datos en crudo en información útil para el análisis, mediante un proceso estructurado que incluye validación, enriquecimiento geográfico, generación de indicadores clave y evaluación de la calidad del procesamiento. Este proyecto forma parte de una prueba técnica para una vacante de ingeniería de datos.

## Arquitectura

El pipeline se divide en las siguientes capas:

- **Raw Layer**: Lectura y almacenamiento de los datos originales obtenidos desde un bucket público en AWS S3, sin modificaciones.
- **Trusted Layer**: Limpieza y validación de datos; se filtran registros erróneos, se corrigen outliers y se enriquecen los datos con información de zonas de taxi.
- **Observability Layer**: Generación de métricas clave del proceso de limpieza como número total de registros, registros descartados, válidos y tiempos de ejecución.
- **Refined Layer**: Transformaciones analíticas y agregación de KPIs para evaluar el comportamiento del sistema de taxis en la ciudad.

## Tecnologías utilizadas

- Python 3.13
- Apache Spark (PySpark)
- AWS S3 (Open Data)
- Git y GitHub

## Estructura del proyecto

```
nyc-yellow-taxi-etl-pipeline/
├── raw/                      # Scripts de extracción de datos desde AWS S3
├── trusted/                  # Limpieza, validación y enriquecimiento de los datos crudos
├── observability/            # Scripts para métricas de ejecución y control de calidad de datos
├── refined/                  # Cálculo y almacenamiento de KPIs para análisis
│   ├── kpi_demand_peak_hours.py
│   ├── kpi_geoeconomic_efficiency.py
│   └── kpi_data_quality_impact.py
├── utils/                    # Funciones auxiliares como logs y validaciones
├── config/                   # Archivos de configuración del pipeline
├── data/                     # Archivos .parquet y reportes generados por cada capa
│   ├── cleaned_2024.parquet
│   ├── observability_report.json
│   └── kpis/
│       ├── kpi_demand_peak_hours.parquet
│       ├── kpi_geoeconomic_efficiency.parquet
│       └── kpi_data_quality_impact.parquet
├── requirements.txt          # Dependencias del entorno para ejecutar el proyecto
├── execution_report.json     # Reporte automatizado con información general del pipeline
└── README.md                 # Documentación general del proyecto
```

---

## Trusted Layer

Esta capa contiene los datos crudos procesados y limpiados. El script `clean_trusted.py` realiza las siguientes acciones:

- Carga los datos `.parquet` desde la carpeta `RAW`.
- Aplica filtros para eliminar registros inválidos o incompletos.
- Verifica que los tipos de datos sean correctos.
- Guarda los datos limpios en `data/cleaned_2024.parquet`.

**Total de registros limpios:** 2.869.714

---

## Observability Layer

El script `observability_metrics.py` evalúa la calidad y el rendimiento del proceso de limpieza de la capa Trusted. Este módulo genera un reporte con:

- Tiempos de inicio y fin de ejecución.
- Total de registros procesados.
- Registros válidos (tras revalidación de criterios).
- Registros descartados.
- Tiempo total de ejecución (en segundos).

El reporte se almacena en formato JSON en la ruta: `data/observability_report.json`.

---

## Refined Layer

En esta capa se realizan transformaciones analíticas sobre los datos limpios para generar indicadores clave de desempeño (KPIs), que permiten evaluar el comportamiento del sistema de taxis amarillos en Nueva York durante 2024.

Los scripts de esta capa son:

### 1. `kpi_demand_peak_hours.py`

Calcula indicadores relacionados con los patrones de demanda:

- Viajes totales por hora del día.
- Días y horarios con mayor concentración de demanda.
- Identificación de horas pico.
- KPIs agregados de viajes por día de la semana.

Los resultados se guardan en:  
`data/kpis/kpi_demand_peak_hours.parquet`

---

### 2. `kpi_geoeconomic_efficiency.py`

Evalúa la eficiencia operativa del sistema desde una perspectiva geográfica y económica:

- Ingreso promedio por zona de recogida.
- Relación entre distancia recorrida y valor del viaje.
- Tarifa promedio por kilómetro.
- Zonas con mayor y menor eficiencia en términos de ingresos.

Los resultados se guardan en:  
`data/kpis/kpi_geoeconomic_efficiency.parquet`

---

### 3. `kpi_data_quality_impact.py`

Analiza el impacto que tiene la calidad de los datos en los resultados de negocio:

- Comparación de KPIs antes y después de la limpieza.
- Porcentaje de reducción de registros por validaciones.
- Estimación del ingreso afectado por registros descartados.

Los resultados se guardan en:  
`data/kpis/kpi_data_quality_impact.parquet`

---

## Cómo ejecutar el pipeline

1. Asegúrate de tener instaladas las dependencias desde `requirements.txt`.
2. Ejecuta cada script por capa, en orden:
   - `raw/extract_raw.py`
   - `trusted/clean_trusted.py`
   - `observability/observability_metrics.py`
   - Los scripts de la capa `refined/`.


**Última actualización:** Abril de 2025.
