import streamlit as st
import requests
import pandas as pd


def cadastra_emprestimo(data):
    url = "http://127.0.0.1:5000/emprestimos"
    r = requests.post(url, json=data)
    return r.status_code


st.set_page_config(page_title="Novo Empréstimo")

st.title(f"Cadastrar novo empréstimo")

id_usuario = st.text_input("Id do usuário:", placeholder="Digite um id do usuário...")

id_bicicleta = st.text_input("Id da bicicleta:", placeholder="Digite um id da bicicleta...")

data_alugado = st.text_input("Data do aluguel:", placeholder="Digite uma data do aluguel...")

if st.button("Enviar:"):
    data = {}

    if id_usuario:
        data["id_usuario"] = id_usuario

    if id_bicicleta:
        data["id_bicicleta"] = id_bicicleta

    if data_alugado:
        data["data_alugado"] = data_alugado

    if len(data) == 3:
        status_code = cadastra_emprestimo(data)

        if status_code in [200, 201]:
            st.success(f"Empréstimo cadastrado com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
    else:
        st.error("Por favor, insira todos os dados para cadastrar um empréstimo.")