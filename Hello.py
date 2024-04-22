import streamlit as st
import requests


st.set_page_config(page_title="Hello")

url = "http://127.0.0.1:5000/"

st.title("Empréstimo de bicicletas")

st.write("Fique a vontade para usar nosso site para aluguar uma bicicleta para uso pessoal")

st.write(":red[AVISO: Para essa aplicação front-end funcionar, é necessário que o back-end esteja rodando localmente em seu dispositivo]")