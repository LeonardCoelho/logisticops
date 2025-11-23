# src/config.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data_raw"
PROCESSED_DATA = BASE_DIR / "data_processed"
DB_PATH = BASE_DIR / "db" / "logisticops.db"

TABLE_NAME = "cargas_logisticas"
LOG_PATH = BASE_DIR / "logs" / "pipeline.log"