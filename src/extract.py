# src/extract.py
import pandas as pd
from config import RAW_DATA
import logging

def load_excel():
    try:
        file = list(RAW_DATA.glob("*.xlsx"))[0]
        df = pd.read_excel(file)
        logging.info(f"Arquivo carregado: {file.name}")
        return df
    except Exception as e:
        logging.error(f"Erro ao carregar planilha: {e}")
        raise