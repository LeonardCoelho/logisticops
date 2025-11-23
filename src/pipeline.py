# src/pipeline.py
import logging
from config import LOG_PATH
from extract import load_excel
from transform import clean_df
from load import save_to_parquet, save_to_sqlite

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    logging.info("Pipeline iniciado.")
    df = load_excel()
    df = clean_df(df)
    save_to_parquet(df)
    save_to_sqlite(df)
    logging.info("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    run()