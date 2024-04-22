import streamlit as st
import requests
import pandas as pd


def get_usuario(id):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//usuarios/{id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()["usuarios"][0]
    elif response.status_code in [400, 404]:
        return {}
    else:
        return None
    

def atualiza_usuario(id, data):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//usuarios/{id}"
    r = requests.put(url, json=data)
    return r.status_code


def excluir_usuario(id):
    url = f"https://aps5-prog-eficaz-back-end.onrender.com//usuarios/{id}"
    r = requests.delete(url)
    return r.status_code


st.set_page_config(page_title="Dados Usuario")

st.title(f"Dados do usuário")
id = st.text_input("Id:", placeholder="Digite um id...")

if st.button("Buscar:"):
    if id:
        st.session_state['usuario'] = get_usuario(id)
    else:
        st.warning("Por favor, insira um id válido.")

if "usuario" in st.session_state and st.session_state['usuario']:
    nome = st.text_input("Nome:", st.session_state['usuario']["nome"])

    cpf = st.text_input("CPF:", st.session_state['usuario']["cpf"])

    data_nascimento = st.text_input("Data de nascimento:", st.session_state['usuario']["data_nascimento"])

    if st.button("Atualizar dados do usuário"):
        data = {}

        if nome != st.session_state['usuario']["nome"]:
            data["nome"] = nome

        if cpf != st.session_state['usuario']["cpf"]:
            data["cpf"] = cpf

        if data_nascimento != st.session_state['usuario']["data_nascimento"]:
            data["data_nascimento"] = data_nascimento

        if len(data) > 0:
            status_code = atualiza_usuario(st.session_state['usuario']["id"], data)

            if status_code == 200:
                del st.session_state['usuario']
                st.success(f"Usuário atualizado com sucesso")
            else:
                st.error(f"Erro {status_code}. Por favor, tente novamente.")
        else:
            st.error("Por favor, altere algum dos dados para atualizar o usuario.")

    if st.button("Excluir usuário"):
        status_code = excluir_usuario(st.session_state['usuario']["id"])

        if status_code == 200:
            del st.session_state['usuario']
            st.success(f"Usuário excluido com sucesso")
        else:
            st.error(f"Erro {status_code}. Por favor, tente novamente.")
            
elif "usuario" in st.session_state and st.session_state['usuario'] == {}:
    st.warning("Id não encontrado ou inválido. Por favor, verifique e tente novamente.")
elif "usuario" in st.session_state and not st.session_state['usuario']:
    st.warning("Erro 500! Por favor, tente novamente mais tarde.")