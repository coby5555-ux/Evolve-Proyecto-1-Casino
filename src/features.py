import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # Generar feature 1: Outliers
    #Elegimos los 5% y 95% en los limites para detectar outliers porque no hay demasiados datos que no nos puedan interesar
    def detect_outliers(column_name: str) -> pd.DataFrame:
        q1 = df[column_name].quantile(0.05)
        q3 = df[column_name].quantile(0.95)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
        return outliers

    # Generar feature 2: Estadísticas descriptivas
    def calculate_summary_stats(column_name: str) -> pd.Series:
        stats = df[column_name].describe()
        return stats

    # Aplicar las funciones de feature 1 y 2 a cada columna
    for column_name in df.columns:
        outliers = detect_outliers(column_name)
        summary_stats = calculate_summary_stats(column_name)
        
        # Añadimos las nuevas columnas al DataFrame, la de outliers y la de estadísticas
        df[f'Outliers_{column_name}'] = outliers.reset_index(drop=True)
        df[f'Summary_Stats_{column_name}'] = summary_stats
        
    return df