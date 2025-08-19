import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import gspread
from google.oauth2.service_account import Credentials

# ---------------------------
# Conectar ao Google Sheets
# ---------------------------
@st.cache_data
def load_data():
    # Lê as credenciais do secrets
    creds_dict = st.secrets["gcp_service_account"]
    credentials = Credentials.from_service_account_info(creds_dict)
    
    # Autentica no Google Sheets
    client = gspread.authorize(credentials)
    
    # Abre a planilha pelo ID
    spreadsheet = client.open_by_key("1y5-ZqLwmS50rqKeC1RlH3qlL7z359aG0c34nQdd69RM")
    
    sheets = {}
    for worksheet in spreadsheet.worksheets():
        df = pd.DataFrame(worksheet.get_all_records())
        sheets[worksheet.title] = df
    return sheets


# ---------------------------
# Configuração inicial
# ---------------------------
st.set_page_config(page_title="Painel de Controle de Grupos", layout="wide")

st.title("📊 Painel de Controle de Grupos")

# Carregar dados
data = load_data()

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
