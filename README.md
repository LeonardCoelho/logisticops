---
config:
      theme: redux
---

graph TD;
    A[Planilha XLSX] --> B[Extração: extract.py];
    B --> C[Transformação: transform.py];
    C --> D[Load: SQLite + Parquet];
    D --> E[Logs: pipeline.log];
