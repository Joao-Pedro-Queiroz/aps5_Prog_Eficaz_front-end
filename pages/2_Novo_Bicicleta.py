import streamlit as st
import requests
import pandas as pd


def cadastra_bicicleta(data):
    url = "https://aps5-prog-eficaz-back-end.onrender.com//bikes"
    r = requests.post(url, json=data)
    return r.status_code


st.set_page_config(page_title="Nova Bicicleta")

st.title(f"Cadastrar nova bicicleta")

id = st.text_input("ID:", placeholder="Digite um id...")

marca = st.text_input("Marca:", placeholder="Digite uma marca...")

modelo = st.text_input("Modelo:", placeholder="Digite um modelo...")

cidade_alocada = st.text_input("Cidade alocada:", placeholder="Digite uma cidade alocada...")

if st.button("Enviar:"):
    data = {}

    if id:
        data["id"] = int(id)

    if marca:
        data["marca"] = marca

    if modelo:
        data["modelo"] = modelo

    if cidade_alocada:
        data["cidade_alocada"] = cidade_alocada

    if len(data) == 4:
        status_code = cadastra_bicicleta(data)

        if status_code in [200, 201]:
            st.success(f"Bicicleta cadastrado com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
    else:
        st.error("Por favor, insira todos os dados para cadastrar uma bicicleta.")