import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Excluir Empréstimos")

st.title("Excluir empréstimo")

id = st.text_input("Id:", placeholder="Digite um id...")

if st.button("Excluir empréstimo"):
    if id:
        url = f"https://aps5-prog-eficaz-back-end.onrender.com//emprestimos/{id}"
        r = requests.delete(url)
        status_code_resposta = r.status_code

        if status_code_resposta == 200:
            st.success(f"Empréstimo excluido com sucesso")
        elif status_code_resposta == 404:
            st.warning("Id não encontrado ou inválido. Por favor, verifique e tente novamente.")
        elif status_code_resposta == 500:
            st.warning("Erro 500! Por favor, tente novamente mais tarde.")
        else:
            st.error(f"Erro {status_code_resposta}. Por favor, tente novamente.")
    else:
        st.warning("Por favor, insira um id válido.")