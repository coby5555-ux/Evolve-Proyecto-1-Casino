from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw" / "1xBet35kGameRecords.csv"
OUT_PATH = ROOT / "data" / "processed" / "1xBet35kGameRecords_Clean.csv"