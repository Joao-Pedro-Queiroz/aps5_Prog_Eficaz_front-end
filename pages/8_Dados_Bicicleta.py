import streamlit as st
import requests
import pandas as pd


def get_bicicleta(id):
    url = f"http://127.0.0.1:5000/bikes/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code in [400, 404]:
        return {}
    else:
        return None
    

def atualiza_bicicleta(id, data):
    url = f"http://127.0.0.1:5000/bikes/{id}"
    r = requests.put(url, json=data)
    return r.status_code


def excluir_bicicleta(id):
    url = f"http://127.0.0.1:5000/bikes/{id}"
    r = requests.delete(url)
    return r.status_code


st.set_page_config(page_title="Dados Bicicleta")

st.title(f"Dados do bicicleta")
id = st.text_input("Id:", placeholder="Digite um id...")

if st.button("Buscar:"):
    if id:
        st.session_state['bicicleta'] = get_bicicleta(id)
    else:
        st.warning("Por favor, insira um id válido.")

if "bicicleta" in st.session_state and st.session_state['bicicleta']['bicicleta_aps_5']:
    marca = st.text_input("Marca:", st.session_state['bicicleta']['bicicleta_aps_5']["marca"])

    modelo = st.text_input("Modelo:", st.session_state['bicicleta']['bicicleta_aps_5']["modelo"])

    cidade_alocada = st.text_input("Cidade alocada:", st.session_state['bicicleta']['bicicleta_aps_5']["cidade_alocada"])

    if st.button("Atualizar dados do livro"):
        data = {}

        if marca != st.session_state['bicicleta']['bicicleta_aps_5']["marca"]:
            data["marca"] = marca

        if modelo != st.session_state['bicicleta']['bicicleta_aps_5']["modelo"]:
            data["modelo"] = modelo

        if cidade_alocada != st.session_state['bicicleta']['bicicleta_aps_5']["cidade_alocada"]:
            data["cidade_alocada"] = cidade_alocada

        if len(data) > 0:
            status_code = atualiza_bicicleta(st.session_state['bicicleta']['bicicleta_aps_5']["id"], data)

            if status_code == 200:
                del st.session_state['bicicleta']
                st.success(f"Bicicleta atualizado com sucesso")
            else:
                st.error(f"Erro {status_code}. Por favor, tente novamente.")
        else:
            st.error("Por favor, altere algum dos dados para atualizar o usuario.")

    if st.button("Excluir livro"):
        status_code = excluir_bicicleta(st.session_state['bicicleta']['bicicleta_aps_5']["id"])

        if status_code == 200:
            del st.session_state['bicicleta']
            st.success(f"Bicicleta excluido com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
            
elif "bicicleta" in st.session_state and st.session_state['bicicleta']['bicicleta_aps_5'] == {}:
    st.warning("Id não encontrado ou inválido. Por favor, verifique e tente novamente.")
elif "bicicleta" in st.session_state and not st.session_state['bicicleta']['bicicleta_aps_5']:
    st.warning("Erro 500! Por favor, tente novamente mais tarde.")