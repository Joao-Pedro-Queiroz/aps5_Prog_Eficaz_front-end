import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Lista Usuarios")

url = "http://127.0.0.1:5000/usuarios"

r = requests.get(url)
status_code_resposta = r.status_code

if status_code_resposta == 200:
    usuário = r.json()

    st.title("Usuários cadastrados/Meus usuários")

    df = pd.DataFrame(usuário["usuarios"])

    st.table(df)
    print(usuário)
elif status_code_resposta == 404:
    st.title(f"Erro 404")
    st.write("API não encontrada! Por favor, tente novamente")
elif status_code_resposta == 500:
    st.title(f"Erro 500")
    st.write("A API está com problema! Por favor, tente novamente mais tarde")
else:
    st.title(f"Erro {status_code_resposta}")
    st.write("Por favor, tente novamente")