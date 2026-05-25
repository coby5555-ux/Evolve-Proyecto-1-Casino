import pandas as pd
import numpy as np
import requests

def clean_null_values(value):
    # Si value es nulo (NaN) devuelve 0
    if pd.isna(value):
        return 0.0
    
def clean_0_values(df):
    # Eliminar filas con todos los valores iguales a 0 porque no tienen sentido en este contexto
    df = df[(df != 0).all(axis=1)]
    return df

def egp_to_eur(df):
    # Obtener la tasa de cambio actual (EGP a EUR) una sola vez (Para no hacer muchas peticiones a la API)
    # Importante saber que esta API es gratis y sin KEY pero solo se puede hacer una peticion cada 20 minutos mas o menos
    url = "https://open.er-api.com/v6/latest/EGP"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extraemos la tasa específica para EUR
        egp_to_eur_rate = data["rates"]["EUR"]
    except Exception as e:
        raise Exception(f"No se pudo obtener la tasa de cambio de la API: {e}")

    # Se definen las columnas que queremos convertir (Las que son de dinero unicamente)
    columnas_a_convertir = [
        'Total Bets', 
        'Total Winnings', 
        'Casino Earnings', 
        'Casino Cumulative Earnings'
    ]

    # Asegurarse de que los datos sean numéricos y multiplicar por la tasa
    # (Uso pd.to_numeric por si acaso había strings o datos mal formateados)
    for col in columnas_a_convertir:
        df[col] = pd.to_numeric(df[col], errors='coerce') * egp_to_eur_rate

    # Redondeo de los resultados a 2 decimales:
    df[columnas_a_convertir] = df[columnas_a_convertir].round(2)

def clean_dates(df, column_name):
    #Convertimos la fecha del Timestamp, y con errors='coerce' hacemos que los nulos devuelvan NaT para manejar los errores mejor
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df

def fix_massive_numbers(df):
    # Cambiamos el formato porque en caso de no hacerlo, hay números demasiado grandes que se representarían en notación científica
    pd.options.display.float_format = '{:.2f}'.format
    return df

