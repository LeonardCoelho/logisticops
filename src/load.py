# src/load.py
from config import DB_PATH, PROCESSED_DATA, TABLE_NAME
import pandas as pd
import sqlite3
import logging

def save_to_parquet(df):
    path = PROCESSED_DATA / "cargas.parquet"
    df.to_parquet(path, index=False)
    logging.info(f"Parquet salvo em {path}")

def save_to_sqlite(df):
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)
    conn.close()
    logging.info(f"Tabela '{TABLE_NAME}' salva em SQLite.")