import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# ---------------------- Dados ----------------------
@st.cache_data
def carregar_dados():
    query = "SELECT * FROM gastos"
    df = pd.read_sql(query, engine)
    df['data'] = pd.to_datetime(df['data'])
    return df

df = carregar_dados()

# ---------------------- Sidebar ----------------------
st.sidebar.title("Filtros")
tipo = st.sidebar.selectbox("Tipo", ["Todos", "Receita", "Despesa"])
categoria = st.sidebar.multiselect("Categoria", options=df["categoria"].unique(), default=df["categoria"].unique())

df_filtrado = df.copy()
if tipo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"].str.lower() == tipo.lower()]

if categoria:
    df_filtrado = df_filtrado[df_filtrado["categoria"].isin(categoria)]

# ---------------------- KPIs ----------------------
st.title("💰 Análise de Gastos Pessoais")

total_receita = df_filtrado[df_filtrado["tipo"].str.lower() == "receita"]["valor"].sum()
total_despesa = df_filtrado[df_filtrado["tipo"].str.lower() == "despesa"]["valor"].sum()
saldo = total_receita - total_despesa

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {total_receita:,.2f}")
col2.metric("Despesa Total", f"R$ {total_despesa:,.2f}")
col3.metric("Saldo", f"R$ {saldo:,.2f}", delta=None if saldo >= 0 else f"-{abs(saldo):,.2f}")

# ---------------------- Gráficos ----------------------
st.subheader("Gastos por Categoria")
gastos_categoria = df_filtrado[df_filtrado["tipo"].str.lower() == "despesa"].groupby("categoria")["valor"].sum()
st.bar_chart(gastos_categoria)

st.subheader("Evolução ao Longo do Tempo")
evolucao = df_filtrado.groupby(df_filtrado["data"].dt.to_period("M"))["valor"].sum()
evolucao.index = evolucao.index.astype(str)
st.line_chart(evolucao)
