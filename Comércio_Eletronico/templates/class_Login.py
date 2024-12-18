import streamlit as st
from controle import Controle
import time

class UI_Login:
    def main():
        st.header("Conecte-se")
        email = st.text_input("Digite o email: ")
        senha = st.text_input("Digite o senha: ",type = "password")
        login, pessoa = Controle.Autentification(email,senha)
        if st.button("Entar"):
            if email and senha:
                if login is None:
                    st.error("Email ou senha invalidos")
                else:
                    # st.write(pessoa)
                    st.session_state["clienteId"] = login["id"]
                    st.session_state["clienteNome"] = login["nome"]
                    return pessoa
            else:
                st.warning("Por favor, preencha todos os campos!")
        