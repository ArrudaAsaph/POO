import streamlit as st
from controle import Controle
import pandas as pd
import time
import json



class UI_Clientes:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])

        with tab1:
            st.header("Lista de Clientes Cadastrados!")
            with open("clientes.json", "r") as f:
                dados_json = json.load(f)

            df = pd.DataFrame(dados_json)

            df = df.drop(columns=["senha"])

            df = df.drop(columns=[])

            st.write("Tabela de Clientes")

            st.dataframe(df, use_container_width=True)
            
        with tab2:
            st.header("Cadastra Novo Cliente!")
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
        
            
            if st.button("Inserir Cliente"):
                #  Cliente_Validation(cls,nome,teletelefone,email,senha
                Controle.Cliente_Validation(nome, telefone, email,senha)
                st.success("Conta criada com sucesso!")
                time.sleep(2)
                st.rerun()

        with tab3:
            st.header("Atualizar Clientes!")
            with open("clientes.json", "r") as f:
                dados_json = json.load(f)

            clientes_nomes = [(cliente["id"],cliente["nome"]) for cliente in dados_json]

            # Usando selectbox para escolher um cliente
            nome_cliente_selecionado = st.selectbox("Escolha um cliente para atualizar:", clientes_nomes)

            # Exibir o cliente selecionado
            st.write(f'Cliente selecionado: {nome_cliente_selecionado}')

            # Encontrar o cliente correspondente ao nome selecionado
            cliente_atualizado = next(cliente for cliente in dados_json if (cliente["id"],cliente["nome"]) == nome_cliente_selecionado)

            # Exibir dados do cliente selecionado para atualizar (pode usar st.text_input, st.text_area, etc.)
            st.write(f"Dados do Cliente: {cliente_atualizado}")