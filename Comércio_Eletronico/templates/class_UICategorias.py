import streamlit as st
from controle import Controle
import pandas as pd
import time
import json



class UI_Categorias:
    def main():
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Adicionar", "Atualizar", "Excluir"])

        with tab1:
            UI_Categorias.Listar()
            
        with tab2:
            UI_Categorias.Adicionar()

        with tab3:
            UI_Categorias.Atualizar()

        with tab4:
            UI_Categorias.Excluir()
    
    def Listar():
        Categorias = Controle.Categoria_Listar()
        if len(Categorias) == 0:
            st.write("Nenhum Categoria cadastrado")
        else:
            st.header("Lista de Categorias Cadastrados!")
            with open("Categorias.json", "r") as f:
                dados_json = json.load(f)

            df = pd.DataFrame(dados_json)


            df = df.drop(columns=[])



            st.write("Tabela de Categorias")

            st.dataframe(df, use_container_width=True)
        
    def Adicionar():
        st.header("Cadastra Novo Categoria!")
        descricao = st.text_input("Infome o descricao: ")
    
        if st.button("Inserir Categoria"):
            #  Categoria_Validation(cls,descricao,teletelefone,email,senha
            Controle.Categoria_Validation_Description(descricao)
            st.success("Categoria criada com sucesso!")
            time.sleep(2)
            st.rerun()
    
    def Atualizar():
        st.header("Atualizar Categoria!")
        Categorias = Controle.Categoria_Listar()
        if len(Categorias) == 0:
            st.write("Nenhum Categoria cadastrado")
        else:
            op = st.selectbox("Selecione o Categoria", Categorias)
            descricao = st.text_input("Informe o descricao: ", op.descricao)
            if st.button("Atualizar"):
                Controle.Categoria_Atualizar(op.id, descricao)
                st.success("Categoria atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
    def Excluir():
        st.header("Remover Categoria!")
        Categorias = Controle.Categoria_Listar()
        if len(Categorias) == 0: 
            st.write("Nenhum Categoria cadastrado")
        else:
            op = st.selectbox("Exclusão de Categoria", Categorias)
            if st.button("Excluir"):
                Controle.Categoria_Excluir(op.id)
                st.success("Categoria excluido com sucesso!")
                time.sleep(2)
                st.rerun()