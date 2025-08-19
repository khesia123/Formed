
❌ **NÃO suba o arquivo `service_account.json`**, ele contém sua chave secreta.

---

### 2. Criar conta de serviço no Google Cloud
1. Vá até [Google Cloud Console](https://console.cloud.google.com/).
2. Ative as APIs:
   - **Google Sheets API**
   - **Google Drive API**
3. Crie uma conta de serviço e faça download do arquivo JSON.
4. Copie o **e-mail da conta de serviço** (exemplo: `formed@formed-469516.iam.gserviceaccount.com`).

---

### 3. Compartilhar a planilha
1. Abra a planilha no Google Sheets.
2. Clique em **Compartilhar**.
3. Adicione o **e-mail da conta de serviço** com permissão de **Editor**.

---

### 4. Configurar Secrets no Streamlit Cloud
1. Vá até [Streamlit Cloud](https://share.streamlit.io/).
2. Vá em **App → Settings → Secrets**.
3. Cole o seguinte conteúdo (substitua `SHEET_ID` pelo ID da sua planilha):

```toml
[gcp_service_account]
type = "service_account"
project_id = "formed-469516"
private_key_id = "fa7d1d0beeedc7879f1163ee4baf968a60697ccc"
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDrZJtpdJWgocQd\nIRUkeEFjXG0jWNEC4zA9hl7Yzt/YxpUviYASzam1956hNk0YkgeWwzgFJJP1nVIt\njUUmkg2VG36kV/UXUkf+bHB/3tvsYWNCcfRQsep2xQ9pFANTX7/951dCKnsTV3OL\nmyxVpk3SDdnDOdGlsuYdUwjLwjBTDq5vWU0XgzoGhfoWdCdhUckHzTmkL72ZKYIf\ngwzf0jhNRp0vv/Mj9Y54KKk16zfRcR+9ndMz+BKvOb3wQL4KdFiOtlbgDHo+lXCZ\nxiGVW1ON3c9dkjfMTu5w5KbW2y0Q8wYKv03tKWXBfBkojZGHarTy8WRp3cc65l4A\nKj+GAyehAgMBAAECgf8fPgwew/qI/u97bkTh/ZQKh1YpqAesVMoffnvJKQZb4v+L\n6CMg8lv/W9ESGFmI3CQ4iazU1LyZ6g0tPpS0qddUmo+6HnJ98xkXVv4mkTcjF6RL\nlOctIX8koobUYhlDm2DWskkVZqDU32pPDEeI8QQUGz6+tAoZsh9F33YNSfMy1m3k\nML7clCGkvP9OrO4mIXU0LxoyNZ11dS4ErWzyyPXBgOr3jDV+xBikBt0GBblUd31U\nizwfysXw3jaqxguJPb6eFRHzin6ON7gqajhTRAvwoveXYc/Ak/itt0I7AZe4OOmp\nUmXjXGAADZeJCS6bnY8dAYzZQtp/df4SJqKckKECgYEA+cFtiszCBG+HxaiOJcob\nHHd8F+0aNTe3WlgLKU2c/h9PZXND8XgilQ9CptJp7Y5WeLqUJxiuo+0INBjVwDGC\n6ILLRWtrYIJx7f9IvKM+narmRMYtDPFKqTs3BX1GGpoVpX2HRHm5VDl3Dx+sjncX\n6qhMF8+n2FKj+9UAK+6k4BECgYEA8UdANVoYZ5qF7LtDcor0RuDoK4mic1Xfd3U5\nRIN94Z7d68i12Oge9TzChdwVcmA/aY1lCKGX4B95ck8tVyT0a2ewe4NqKnVZARKU\nowLzEtjjhYzXherAU+VvK09/eCNGvxuZpV5uJDH47sbuxntibe9M7KMqmrAK1dL/\nFcS6XpECgYAA4lZo72Cgc2SfpoEaUSTXbPTbgNNe7NuRTk57zvKHU8UMLuRGro4w\nyOULgiMt3BsiQkbT/Jphqi0lQhE/pO05tXzSuhafONb+aLDxOgK2vCwkgi8WpKQH\nBVakhlUBMxpwg4k/DM9DJRDu1MXfmzxScFYUn3+QnHpIIfDmNuoOgQKBgBWiAcvG\nzDFd1WwoTh/S/ZvtRmPA72PP6z1WsU/HSl4UVGlzkXplNYFfdUFzPikHIChimRBx\nDKD3sXfiSXpqwc9veI9adQZhhx1lgRYsiYbDE4NB4YEMTzo2dAU6F3+6CfnQi7Ic\nCVwNbvhZtcbuASFCN29wIb3E0vPg+yYEgYFBAoGAEs1YFjPptRVHyJenmaom0E65\n5h2GaigoWjxchBX8gZgWHyPIUfiD54hjd2BTjGgVTRmc9+MpM0Wu08abhuYv4+qe\nqD8HUr46EifzLIg0PJDSpxjwZe68FxT+t7kQWOxqW2FowneFOT0ChXHrxNJT24+7\n/XXmy2InYgt9wCDSYEc=\n-----END PRIVATE KEY-----\n"
client_email = "formed@formed-469516.iam.gserviceaccount.com"
client_id = "103408189287035834442"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/formed%40formed-469516.iam.gserviceaccount.com"
universe_domain = "googleapis.com"

[app]
SHEET_ID = "COLOQUE_AQUI_O_ID_DA_PLANILHA"
