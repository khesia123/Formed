import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Carregar planilha
# ---------------------------
@st.cache_data
def load_data(file):
    xls = pd.ExcelFile(file)
    sheets = {}
    for sheet in xls.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)
        # Corrigir cabeçalho (primeira linha como nomes de coluna)
        df.columns = df.iloc[0]
        df = df.drop(0).reset_index(drop=True)
        sheets[sheet] = df
    return sheets

st.set_page_config(page_title="Painel de Controle de Grupos", layout="wide")

st.title("📊 Painel de Controle de Grupos")

# Upload do arquivo
uploaded_file = st.file_uploader("Carregue a planilha Excel", type=["xlsx"])

if uploaded_file:
    data = load_data(uploaded_file)

    # Menu lateral para escolher aba
    sheet_name = st.sidebar.selectbox("Escolha a aba", list(data.keys()))

    df = data[sheet_name]
    st.subheader(f"📂 Dados da aba: {sheet_name}")
    st.dataframe(df, use_container_width=True)

    # ---------------------------
    # Gráficos básicos
    # ---------------------------
    if "SATISFAÇÃO DO CLIENTE" in df.columns:
        st.subheader("📌 Satisfação dos Clientes")
        fig, ax = plt.subplots()
        df["SATISFAÇÃO DO CLIENTE"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    if "QUALIDADE DO LEAD" in df.columns:
        st.subheader("📌 Qualidade dos Leads")
        fig, ax = plt.subplots()
        df["QUALIDADE DO LEAD"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    if "CAMPANHA ESTÁ ATIVA?" in df.columns:
        st.subheader("📌 Status das Campanhas")
        fig, ax = plt.subplots()
        df["CAMPANHA ESTÁ ATIVA?"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

else:
    st.info("⬆️ Faça o upload da planilha para visualizar os dados.")
