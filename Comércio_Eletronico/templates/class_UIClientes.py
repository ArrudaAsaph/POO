import streamlit as st
from controle import Controle
import pandas as pd
import time
import json



class UI_Clientes:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])

        with tab1:
            UI_Clientes.Listar()
            
        with tab2:
            UI_Clientes.Adicionar()

        with tab3:
            UI_Clientes.Atualizar()

        with tab4:
            UI_Clientes.Excluir()
    
    def Listar():
        clientes = Controle.Cliente_Listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            st.header("Lista de Clientes Cadastrados!")
            with open("clientes.json", "r") as f:
                dados_json = json.load(f)

            df = pd.DataFrame(dados_json)

            df = df.drop(columns=["senha"])

            df = df.drop(columns=[])

            df = df.drop(index=0)

            st.write("Tabela de Clientes")

            st.dataframe(df, use_container_width=True)
        
    def Adicionar():
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
    
    def Atualizar():
        st.header("Atualizar Cliente!")
        clientes = Controle.Cliente_Listar()
        clientes = clientes[1:]
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Selecione o cliente", clientes)
            nome = st.text_input("Informe o nome: ", op.nome)
            telefone = st.text_input("Informe o email: ", op.telefone)
            email = st.text_input("Informe o fone: ", op.email)
            senha = st.text_input("Informe a senha: ", op.senha, type="password")
            if st.button("Atualizar"):
                Controle.Cliente_Atualizar(op.id, nome, telefone, email, senha)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    def Excluir():
        st.header("Remover Cliente!")
        clientes = Controle.Cliente_Listar()
        clientes = clientes[1:]
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de cliente", clientes)
            if st.button("Excluir"):
                Controle.Cliente_Excluir(op.id)
                st.success("Cliente excluido com sucesso!")
                time.sleep(2)
                st.rerun()