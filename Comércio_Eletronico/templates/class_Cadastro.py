import streamlit as st
from controle import Controle
import time

class UI_Cadastro:
    def main():
        st.header("Cadastra-se ")
        Controle.Admin()
        UI_Cadastro.inserir()

    def inserir():
        nome = st.text_input("Infome o nome: ")
        if nome:
            nome = Controle.Cliente_Validation_Name(nome)
        telefone = st.text_input("Informe o telefone: ")
        if telefone:
            telefone = Controle.Cliente_Validation_Phone(telefone)

            if not telefone:
                st.error("Número de teletelefone inválido! Ex: DDD + XXXXXXXXX (84981311523)")
            
        email = st.text_input("Informe o email: ")
        if email:
            email = Controle.Cliente_Validation_Email(email)

            if not email:
                st.error("Endereço de email inválido! Ex: xxxxx@xxxx.com (azulvermelho@gmail.com)")

            
        
        senha = st.text_input("Informe a senha: ", type="password")
    
        
        if st.button("Inserir"):
            #  Cliente_Validation(cls,nome,teletelefone,email,senha
            Controle.Cliente_Validation(nome, telefone, email,senha)
            st.success("Conta criada com sucesso!")
            time.sleep(2)
            st.rerun()
            