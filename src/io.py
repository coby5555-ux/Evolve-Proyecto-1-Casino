from pathlib import Path
import pandas as pd

def save_csv(df: pd.DataFrame, file_name: str):
    
    #Guarda el DataFrame procesado en la carpeta data/processed.
    root_path = Path(__file__).parent.parent
    output_dir = root_path / "data" / "processed"

    #Si no existe la carpeta se crea
    output_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = output_dir / file_name
    df.to_csv(file_path, index=False)
    print(f"Los datos han sido guardados correctamente en: {file_path}")

def load_csv(file_name: str) -> pd.DataFrame:
    
    #Carga del dataset en la carpeta data/raw 
    root_path = Path(__file__).parent.parent
    file_path = root_path / "data" / "raw" / file_name
    
    if not file_path.exists():
        raise FileNotFoundError(f"El fichero no fue encontrado en: {file_path}")
        
    print(f"Cargando datos desde: {file_path}")

    return pd.read_csv(file_path)

