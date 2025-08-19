import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request

st.set_page_config(page_title="Painel de Controle de Grupos", layout="wide")
st.title("📊 Painel de Controle de Grupos")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

@st.cache_data(show_spinner="Conectando ao Google…")
def load_data():
    # 1) Credenciais do secrets
    creds_dict = st.secrets["gcp_service_account"]

    # 2) Credenciais com scopes
    credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)

    # 3) Força refresh do token (útil para diagnosticar erros)
    credentials.refresh(Request())

    # 4) Autoriza gspread
    client = gspread.authorize(credentials)

    # 5) Abre a planilha pelo ID guardado em [app]
    sheet_id = st.secrets["app"]["SHEET_ID"]
    spreadsheet = client.open_by_key(sheet_id)

    # 6) Lê todas as abas
    sheets = {}
    for ws in spreadsheet.worksheets():
        df = pd.DataFrame(ws.get_all_records())
        sheets[ws.title] = df
    return sheets

try:
    data = load_data()
except Exception as e:
    st.error("❌ Falha para autenticar/ler a planilha.")
    with st.expander("Ver detalhes do erro (para correção)"):
        st.exception(e)
    st.info(
        "Verifique:\n"
        "1) Secrets TOML no formato acima (private_key com \\n).\n"
        "2) Planilha compartilhada com a conta de serviço como Editor.\n"
        "3) Google Sheets API e Google Drive API habilitadas no GCP.\n"
        "4) Nenhum JSON com segredo foi comitado no GitHub."
    )
    st.stop()

# --- UI ---
sheet_name = st.sidebar.selectbox("Escolha a aba", list(data.keys()))
df = data[sheet_name]

st.subheader(f"📂 Dados da aba: {sheet_name}")
st.dataframe(df, use_container_width=True)

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
