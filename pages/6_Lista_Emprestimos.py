import streamlit as st
import requests
import pandas as pd


st.set_page_config(page_title="Lista Empréstimos")

url = "http://127.0.0.1:5000/emprestimos"

st.title("Empréstimos cadastrados/Meus empréstimos")

st.title("Filtro:")

id_usuario = st.text_input("Id do usuário:", placeholder="Digite um id do usuário...")

id_bicicleta = st.text_input("Id da bicicleta:", placeholder="Digite um id da bicicleta...")

if st.button("Enviar:"):
    if id_usuario and not id_bicicleta:
        url += f"?id_usuario={id_usuario}"

    if id_bicicleta and not id_usuario:
        url += f"?id_bicicleta={id_bicicleta}"

    if id_usuario and id_bicicleta:
        url += f"?id_usuario={id_usuario}&id_bicicleta={id_bicicleta}"

r = requests.get(url)
status_code_resposta = r.status_code

if status_code_resposta == 200:
    emprestimos = r.json()["emprestimos"]

    st.title("Empréstimos cadastrados")

    df = pd.DataFrame(emprestimos)

    st.table(df)
elif status_code_resposta == 404:
    st.title(f"Erro 404")
    st.write("API não encontrado! Por favor, tente novamente")
elif status_code_resposta == 500:
    st.title(f"Erro 500")
    st.write("A API está com problema! Por favor, tente novamente mais tarde")
else:
    st.title(f"Erro {status_code_resposta}")
    st.write("Por favor, tente novamente")