from pathlib import Path
import pandas as pd

def load_day_ahead_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_ENERGY_PRICES_Test_24012025.csv"
    return pd.read_csv(csv_path)

def load_load_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_TOTAL_LOAD_DAYAHEAD_Test_24012025.csv"
    return pd.read_csv(csv_path)