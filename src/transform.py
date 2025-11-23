# src/transform.py
import pandas as pd
import logging

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Iniciando limpeza dos dados...")

    # renomeia colunas para padrão snake_case
    rename_map = {
        "Nº OC": "oc_numero",
        "DATA DA ROT.": "data_rotas",
        "CIDADE + UF": "cidade_uf",
        "CLIENTE": "cliente",
        "DATA AGENDA (SE FOR AGENDADO)": "data_agenda",
        "PALETIZADO SIM OU NÃO": "paletizado",
        "NOME TRANSPORTADORA": "transportadora",
        "PESO": "peso",
        "QUANTIDADE CAIXAS": "qtd_caixas",
        "CUBAGEM": "cubagem",
        "QUANTIDADE ENTREGAS": "qtd_entregas",
        "PERFIL VEÍCULO": "perfil_veiculo",
        "DATA PROGRAMADA CARREGAMENTO": "data_prog_carga"
    }

    df = df.rename(columns=rename_map)

    # converter datas
    date_cols = ["data_rotas", "data_agenda", "data_prog_carga"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], format="%d/%m/%Y", errors="coerce")

    # normalizar campo paletizado
    df["paletizado"] = df["paletizado"].str.upper().map({
        "SIM": 1,
        "NÃO": 0,
        "NAO": 0
    })

    # tipos numéricos
    df["peso"] = pd.to_numeric(df["peso"], errors="coerce")
    df["qtd_caixas"] = pd.to_numeric(df["qtd_caixas"], errors="coerce")
    df["cubagem"] = pd.to_numeric(df["cubagem"], errors="coerce")
    df["qtd_entregas"] = pd.to_numeric(df["qtd_entregas"], errors="coerce")

    # remover duplicados
    df = df.drop_duplicates()

    logging.info("Limpeza concluída.")
    return df