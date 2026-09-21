# Análisis de datos de AquaLimpia S. A.

## Objetivo
Analizar el desempeño de las plantas de tratamiento usando las variables disponibles y generar información útil para Operaciones y Gestión Ambiental.

## Datos
Se utilizó el archivo `dataset_set_A_aguas_residuales.xlsx`. El conjunto contiene 200 registros, 10 variables y datos de tres plantas.

## Metodología
- Carga del Excel con pandas.
- Revisión de valores faltantes y duplicados.
- Cálculo de promedios y porcentajes por planta.
- Revisión de relaciones entre variables.
- Aplicación de pruebas estadísticas exploratorias con SciPy.
- Generación de reportes separados por área.
- Construcción de un dashboard para apoyar la interpretación.

## Resultados
El indicador `cumplimiento_norma` toma el valor 1 en 45 de los 200 registros. La DBO de salida promedio fue 36,18 mg/L. La planta Sur registró 29,6% de valores de cumplimiento, Centro 22,7% y Norte 16,9%.

## Limitaciones
No se informa en el dataset el límite normativo utilizado para construir la variable de cumplimiento. Tampoco se puede concluir causalidad a partir de correlaciones. El período observado va de julio a octubre de 2025, por lo que abarca cuatro meses.

## Conclusión
El análisis permite tener una primera visión del comportamiento de las plantas y entregar indicadores para priorizar revisiones. Para tomar decisiones operativas de mayor impacto sería necesario complementar el dataset con el límite normativo, información de carga contaminante, eventos operacionales y antecedentes de cada planta.
