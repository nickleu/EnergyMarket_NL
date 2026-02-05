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

def load_onshore_wind_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_WIND_SOLAR_GENERATION_FORECAST_ONSHORE_Test_24012025.csv"
    return pd.read_csv(csv_path)

def load_offshore_wind_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_WIND_SOLAR_GENERATION_FORECAST_OFFSHORE_Test_24012025.csv"
    return pd.read_csv(csv_path)

def load_solar_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_WIND_SOLAR_GENERATION_FORECAST_SOLAR_Test_24012025.csv"
    return pd.read_csv(csv_path)

def load_generation_test():
    repo_root = Path(__file__).resolve().parent.parent
    csv_path = repo_root / "Data" / "raw" / "GUI_TOTAL_GENERATION_FORECAST_Test_24012025.csv"
    return pd.read_csv(csv_path)

def load_2025():
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "Data" / "external"

    csv_files = sorted(data_dir.glob("2025_GUI_*.csv"))

    if not csv_files:
        raise FileNotFoundError("No matching CSV files found")

    dfs = []

    for f in csv_files:
        df = pd.read_csv(f)
        dfs.append(df)

    # Horizontal concatenation (columns side by side)
    df_out = pd.concat(dfs, axis=1)

    return df_out

def load_2026():
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "Data" / "external"

    csv_files = sorted(data_dir.glob("2026_GUI_*.csv"))

    if not csv_files:
        raise FileNotFoundError("No matching CSV files found")

    dfs = []

    for f in csv_files:
        df = pd.read_csv(f)
        dfs.append(df)

    # Horizontal concatenation (columns side by side)
    df_out = pd.concat(dfs, axis=1)

    return df_out