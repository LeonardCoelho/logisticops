# src/load_data.py
import pandas as pd
from pathlib import Path
import sqlite3

BASE = Path(__file__).resolve().parent.parent

def load_parquet():
    return pd.read_parquet(BASE / "data_processed" / "cargas.parquet")

def load_sqlite():
    conn = sqlite3.connect(BASE / "db" / "logisticops.db")
    df = pd.read_sql("SELECT * FROM cargas_logisticas", conn)
    conn.close()
    return df