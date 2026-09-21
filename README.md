# Proyecto AquaLimpia S. A. — Ciencia de Datos, Semana 8

## Objetivo
Analizar el comportamiento de las plantas de tratamiento de AquaLimpia S. A. para apoyar la detección de patrones operativos y de cumplimiento.

## Datos
Dataset Excel con 200 registros y 11 variables. El período observado va desde 2025-07-01 hasta 2025-10-28.

## Flujo
1. Carga y revisión del dataset.
2. Evaluación básica de calidad.
3. Cálculo de indicadores por planta.
4. Análisis estadístico exploratorio.
5. Generación de reportes diferenciados.
6. Visualización mediante dashboard.
7. Documentación y control de versiones.

## Resultados principales
- Cumplimiento global según la variable `cumplimiento_norma`: 22.5%.
- DBO de salida promedio: 36.18 mg/L.
- Correlación entre caudal de entrada y energía de aireación: 0.85.
- No se detectaron valores faltantes ni registros duplicados.

## Limitaciones
La variable `cumplimiento_norma` está codificada como 0/1, pero el dataset no incluye en sus columnas una descripción del límite normativo utilizado. Por eso, el análisis la trata como indicador entregado por la fuente y evita inferir un umbral específico de DBO. Además, el período del archivo cubre cuatro meses, por lo que no se debe asumir que representa exactamente un trimestre.

## Archivos
- `src/analisis_principal.py`
- `src/funciones_analisis.py`
- `data/dataset_set_A_aguas_residuales.xlsx`
- `outputs/dashboard_aqualimpia.png`
- `outputs/reporte_operaciones.xlsx`
- `outputs/reporte_gestion_ambiental.xlsx`
- `outputs/resumen_por_planta.xlsx`
- `analisis_principal.ipynb`
