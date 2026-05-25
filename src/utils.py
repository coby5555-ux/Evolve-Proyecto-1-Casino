import pandas as pd

def check_missing_columns(df: pd.DataFrame, required: list[str]) -> None:
    # Chequeo de columnas que faltan
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Columnas faltantes: {missing}')
    print("Validación de columnas exitosa.")    


