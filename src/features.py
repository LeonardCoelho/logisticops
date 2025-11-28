# src/features.py
import pandas as pd

def create_features(df: pd.DataFrame):
    df = df.copy()

    # features temporais
    df["ano"] = df["data_rotas"].dt.year
    df["mes"] = df["data_rotas"].dt.month
    df["dia"] = df["data_rotas"].dt.day
    df["dia_semana"] = df["data_rotas"].dt.dayofweek  # 0 = segunda

    # demanda diária: soma de caixas, peso, entregas
    daily = df.groupby("data_rotas").agg({
        "qtd_caixas": "sum",
        "peso": "sum",
        "qtd_entregas": "sum"
    }).reset_index()

    daily.rename(columns={
        "qtd_caixas": "caixas_dia",
        "peso": "peso_dia",
        "qtd_entregas": "entregas_dia"
    }, inplace=True)

    return df, daily