import streamlit as st
import requests
import pandas as pd


def get_bicicleta(id):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//bikes/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['bicicletas'][0]
    elif response.status_code in [400, 404]:
        return {}
    else:
        return None
    

def atualiza_bicicleta(id, data):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//bikes/{id}"
    r = requests.put(url, json=data)
    return r.status_code


def excluir_bicicleta(id):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//bikes/{id}"
    r = requests.delete(url)
    return r.status_code


st.set_page_config(page_title="Dados Bicicleta")

st.title(f"Dados da bicicleta")
id = st.text_input("Id:", placeholder="Digite um id...")

if st.button("Buscar:"):
    if id:
        st.session_state['bicicleta'] = get_bicicleta(id)
    else:
        st.warning("Por favor, insira um id válido.")

if "bicicleta" in st.session_state and st.session_state['bicicleta']:
    marca = st.text_input("Marca:", st.session_state['bicicleta']["marca"])

    modelo = st.text_input("Modelo:", st.session_state['bicicleta']["modelo"])

    cidade_alocada = st.text_input("Cidade alocada:", st.session_state['bicicleta']["cidade_alocada"])

    status = st.text_input("Status da bicicleta:", st.session_state['bicicleta']["status"])

    if st.button("Atualizar dados da bicicleta"):
        data = {}

        if marca != st.session_state['bicicleta']["marca"]:
            data["marca"] = marca

        if modelo != st.session_state['bicicleta']["modelo"]:
            data["modelo"] = modelo

        if cidade_alocada != st.session_state['bicicleta']["cidade_alocada"]:
            data["cidade_alocada"] = cidade_alocada

        if status != st.session_state['bicicleta']["status"]:
            data["status"] = status

        if len(data) > 0:
            status_code = atualiza_bicicleta(st.session_state['bicicleta']["id"], data)

            if status_code == 200:
                del st.session_state['bicicleta']
                st.success(f"Bicicleta atualizado com sucesso")
            else:
                st.error(f"Erro {status_code}. Por favor, tente novamente.")
        else:
            st.error("Por favor, altere algum dos dados para atualizar o usuario.")

    if st.button("Excluir bicicleta"):
        status_code = excluir_bicicleta(st.session_state['bicicleta']["id"])

        if status_code == 200:
            del st.session_state['bicicleta']
            st.success(f"Bicicleta excluido com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
            
elif "bicicleta" in st.session_state and st.session_state['bicicleta'] == {}:
    st.warning("Id não encontrado ou inválido. Por favor, verifique e tente novamente.")
elif "bicicleta" in st.session_state and not st.session_state['bicicleta']:
    st.warning("Erro 500! Por favor, tente novamente mais tarde.")