import pandas as pd
import numpy as np
from pathlib import Path

def cargar_datos(ruta_archivo):
    """Carga el Excel y deja la fecha en formato datetime."""
    df = pd.read_excel(ruta_archivo)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"])
    return df

def evaluar_calidad(df):
    """Resume aspectos básicos de calidad y consistencia del dataset."""
    return {
        "filas": len(df),
        "columnas": len(df.columns),
        "faltantes": int(df.isna().sum().sum()),
        "duplicados": int(df.duplicated().sum()),
        "plantas": int(df["planta"].nunique()),
        "fecha_min": str(df["fecha_registro"].min().date()),
        "fecha_max": str(df["fecha_registro"].max().date()),
    }

def resumen_por_planta(df):
    """Calcula indicadores principales por planta."""
    datos = df.copy()
    datos["eficiencia_DBO_pct"] = (
        1 - datos["DBO_salida_mg_L"] / datos["DBO_entrada_mg_L"]
    ) * 100
    return (
        datos.groupby("planta")
        .agg(
            registros=("planta","size"),
            caudal_promedio=("caudal_entrada_m3_d","mean"),
            dbo_entrada_promedio=("DBO_entrada_mg_L","mean"),
            dbo_salida_promedio=("DBO_salida_mg_L","mean"),
            energia_promedio=("energia_aeracion_kWh","mean"),
            lodos_promedio=("lodos_generados_kg_d","mean"),
            eficiencia_dbo_promedio=("eficiencia_DBO_pct","mean"),
            cumplimiento_pct=("cumplimiento_norma","mean"),
        )
        .reset_index()
    )

def generar_reportes(df, resumen, carpeta="outputs"):
    """Genera salidas diferenciadas para Operaciones y Gestión Ambiental."""
    out = Path(carpeta)
    out.mkdir(exist_ok=True)
    df[[
        "fecha_registro","planta","caudal_entrada_m3_d",
        "DBO_entrada_mg_L","DBO_salida_mg_L",
        "energia_aeracion_kWh","lodos_generados_kg_d"
    ]].to_excel(out/"reporte_operaciones.xlsx", index=False)

    df[[
        "fecha_registro","planta","DBO_salida_mg_L",
        "cumplimiento_norma"
    ]].to_excel(out/"reporte_gestion_ambiental.xlsx", index=False)

    resumen.to_excel(out/"resumen_por_planta.xlsx", index=False)
