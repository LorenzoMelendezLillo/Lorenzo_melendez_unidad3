import pandas as pd
import numpy as np
from scipy import stats
from joblib import Parallel, delayed
from funciones_analisis import cargar_datos, evaluar_calidad, resumen_por_planta, generar_reportes

RUTA = "data/dataset_set_A_aguas_residuales.xlsx"

def ejecutar():
    df = cargar_datos(RUTA)
    calidad = evaluar_calidad(df)
    resumen = resumen_por_planta(df)

    # Cálculos independientes en paralelo para dejar el flujo preparado para escalar.
    tareas = [
        ("correlacion_caudal_energia", lambda: df["caudal_entrada_m3_d"].corr(df["energia_aeracion_kWh"])),
        ("cumplimiento_global", lambda: df["cumplimiento_norma"].mean() * 100),
        ("dbo_salida_promedio", lambda: df["DBO_salida_mg_L"].mean())
    ]
    resultados = Parallel(n_jobs=-1)(
        delayed(lambda nombre, fn: (nombre, fn()))(nombre, fn) for nombre, fn in tareas
    )

    # Contraste descriptivo/estadístico entre plantas para DBO de salida.
    grupos = [g["DBO_salida_mg_L"].values for _, g in df.groupby("planta")]
    anova = stats.f_oneway(*grupos)

    generar_reportes(df, resumen)
    print("Calidad:", calidad)
    print("Indicadores:", resultados)
    print("ANOVA DBO salida:", anova)
    return df, calidad, resumen

if __name__ == "__main__":
    ejecutar()
