from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.io import save_csv
from src.cleaning import clean_0_values
from src.cleaning import clean_null_values
from src.cleaning import clean_dates
from src.cleaning import egp_to_eur
from src.cleaning import fix_massive_numbers
from src.features import build_features
from src.utils import check_missing_columns
from src.viz import plot_graph


def main():
    # Carga del csv
    df = load_csv(RAW_PATH)
    # Limpieza, ejecutamos las funciones de cleaning
    df = clean_null_values(df)
    df = clean_0_values(df)
    df = clean_dates(df, 'Timestamp')
    df = egp_to_eur(df)
    df = fix_massive_numbers(df)
    # Comprobamos que no faltan columnas
    check_missing_columns(df, ['Timestamp', 'Game ID', 'Game Name', 'Odds', 'Total Bets', 'Total Winnings', 'Total Players', 'Players Lost', 'Casino Earnings', 'Casino Cumulative Earnings'])
    # Construimos las features
    df = build_features(df)
    

    plot_graph(df)

    # Guardamos el csv
    df.save_csv(OUT_PATH)
    print(f"El archivo se ha guardado en: {OUT_PATH}")


if __name__ == "__main__":
    main()
