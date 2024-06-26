import streamlit as st
import requests
import pandas as pd


def cadastra_usuário(data):
    url = "https://aps5-prog-eficaz-back-end.onrender.com//usuarios"
    r = requests.post(url, json=data)
    return r.status_code


st.set_page_config(page_title="Novo Usuario")

st.title(f"Cadastrar novo usuário")

id = st.text_input("ID:", placeholder="Digite um id...")

nome = st.text_input("Nome:", placeholder="Digite um nome...")

cpf = st.text_input("CPF:", placeholder="Digite um cpf...")

data_nascimento = st.text_input("Data de nascimento:", placeholder="Digite uma data de nascimento...")

if st.button("Enviar:"):
    data = {}

    if id:
        data["id"] = int(id)

    if nome:
        data["nome"] = nome

    if cpf:
        data["cpf"] = cpf

    if data_nascimento:
        data["data_nascimento"] = data_nascimento

    if len(data) == 4:
        status_code = cadastra_usuário(data)

        if status_code in [200, 201]:
            st.success(f"Usuario cadastrado com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
    else:
        st.error("Por favor, insira todos os dados para cadastrar um usuário.")