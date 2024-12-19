import streamlit as st
from controle import Controle
import pandas as pd
import time
import json



class UI_Produtos:
    def main():
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Adicionar", "Atualizar", "Reajuste","Excluir"])

        with tab1:
            UI_Produtos.Listar()
            
        with tab2:
            UI_Produtos.Adicionar()

        with tab3:
            UI_Produtos.Atualizar()

        with tab4:
            UI_Produtos.Reajuste()

        with tab5:
            UI_Produtos.Excluir()
    
    def Listar():
        Produtos = Controle.Produto_Listar()
        if len(Produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            st.header("Lista de Produtos Cadastrados!")
            with open("Produtos.json", "r") as f:
                dados_json = json.load(f)

            df = pd.DataFrame(dados_json)


            df = df.drop(columns=[])



            st.write("Tabela de Produtos")

            st.dataframe(df, use_container_width=True)
        
    def Adicionar():
        st.header("Cadastra Novo Produto!")

        nome_produto = st.text_input("Informe o nome do Produto: ")
        preco = st.number_input("Informe o preço do Produto: R$")
        
        estoque = st.number_input("Informe o estoque do Produto: ", min_value=0, step=1, format="%d")

        categorias = Controle.Categoria_Listar()
        if len(categorias) == 0:
            st.write("Nenhum Categoria cadastrado")
        else:
            list_categorias = []
            for categoria in categorias:
                list_categorias.append(categoria.descricao)
            id_Categoria = st.selectbox(
                "Selecione a Categoria",
                options=[None] + list_categorias,  
                format_func=lambda x: "Selecione uma Categoria" if x is None else x,  
                key="categoria_selecao")

            nova_categoria = st.text_input("Categoria do Produto: ",id_Categoria)
            
            if st.button("Inserir Produto"):

                if nova_categoria:
                    if nova_categoria not in list_categorias:
                        Controle.Categoria_Validation_Description(nova_categoria)
                        id_Categoria = nova_categoria

                categorias = Controle.Categoria_Listar()

                for categoria in categorias:
                    if categoria.descricao == id_Categoria:
                        id_Categoria = categoria.id
                
                if not nome_produto or preco <= 0 or estoque <= 0 or not id_Categoria:
                    st.error("Complete todos os campos do cadastro! ")
                else:
                    Controle.Produto_Validation(nome_produto,preco,estoque,id_Categoria)
                    st.success("Produto criado com sucesso!")
                    time.sleep(2)
                    st.rerun()   
    
    def Atualizar():
        st.header("Atualizar Produtos")      

        Produtos = Controle.Produto_Listar()
        if len(Produtos) == 0:
            st.write("Nenhum Produto cadastrado")
        else:
            op = st.selectbox("Selecione o Produto", Produtos)
            descricao = st.text_input("Informe a nova descricao: ", op.descricao)
            preco = st.number_input("Informe o novo preço: R$ ", op.preco)
            estoque = st.number_input("Informe o novo estoque: ", op.estoque)
            categorias = Controle.Categoria_Listar()
            if len(categorias) == 0:
                st.write("Nenhum Categoria cadastrado")
            else:
                id_cat = op.id_categoria
                list_categorias = []
                for categoria in categorias:
                    if categoria.id == op.id_categoria:
                        id_cat = categoria.descricao
                    else:
                        list_categorias.append(categoria.descricao)
                
                nov_id_Categoria = st.selectbox(
                    "Selecione a nova Categoria",
                    options=[id_cat] + list_categorias,
                    format_func=lambda x: "Selecione uma Categoria" if x is None else x,
                    key="selecao_categoria_unica"
                )
            if st.button("Atualizar Produto"):
                
                categorias = Controle.Categoria_Listar()

                for categoria in categorias:
                    if categoria.descricao == nov_id_Categoria:
                        id_Categoria = categoria.id
                
                if not descricao or preco <= 0 or estoque <= 0 or not id_Categoria:
                    st.error("Complete todos os campos do cadastro! ")
                else:
                    Controle.Produto_Atualizar(op.id,descricao,preco,estoque,id_Categoria)
                    st.success("Produto criado com sucesso!")
                    time.sleep(2)
                    st.rerun()
             
    def Excluir():
        st.header("Remover Produto!")
        Produtos = Controle.Produto_Listar()
        if len(Produtos) == 0: 
            st.write("Nenhum Produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produto", Produtos)
            if st.button("Excluir"):
                Controle.Produto_Excluir(op.id)
                st.success("Produto excluido com sucesso!")
                time.sleep(2)
                st.rerun()
    def Reajuste():
        st.header("Reajuste dos Produtos!")
        botao_espefico, botao_geral = st.tabs(["Específico","Geral"])
        

       

        with botao_espefico:     
            Produtos = Controle.Produto_Listar()
            list_produtos = [produto.descricao for produto in Produtos]

            if len(Produtos) == 0:
                st.write("Nenhum Produto cadastrado")
            else:
                operacao = st.selectbox(
                    "Selecione o Produto",
                    options=[None] + list_produtos,
                    format_func=lambda x: "Selecione o Produto" if x is None else x,
                    key="operacao_produto"
                )
                valor = next((produto.preco for produto in Produtos if produto.descricao == operacao), None)
                for produto in Produtos:
                    if produto.descricao == operacao:
                        id = produto.id

            if operacao:
                st.markdown(f"### Preço do {operacao} = R$ {valor}")
                
                
            else:
                st.write("Selecione um produto para continuar.")

            # c1, c2 = st.columns(2)
            # with c1:
          

           
            valor_reajuste_por = st.number_input(
                "Informe o aumento do produto (%):",
                min_value=-100, max_value=100, value=0, key="input_porcentagem"
            )
            if valor_reajuste_por != 0:
                if valor_reajuste_por < 0:
                    st.markdown(f"##### Decrecimo de {valor_reajuste_por}%")
                    
                else:
                    st.markdown(f"##### Acréscimo de {valor_reajuste_por}%")
                st.markdown(f"#### Novo Preço do {operacao} = {valor + (valor * (valor_reajuste_por/100))} -> Dif: {valor - valor + (valor * (valor_reajuste_por/100))}  ")
                valor_reajuste = valor_reajuste_por


    
            if st.button("Reajustar o preço!"):
                if valor_reajuste_por == 0:
                    st.error("Preencha o campo para atualizar o produto!")
                else:
                    percentual = valor_reajuste / 100
                    Controle.Reajustar_Produto_Unico(id,percentual)
                    st.success("Produto atualizado com sucesso!")


        with botao_geral:
            st.markdown(f"### Aumenta o preço de todos os produtos cadastrados!")
            valor_reajuste_porcentagem_total = st.number_input(
                    "Informe o aumento do produto (%):",
                    min_value=-100, max_value=100, value=0, key="input_porcentagem_totalcentagem"
                )
            if st.button("Reajustar o preço dos produtos!"):
                if valor_reajuste_porcentagem_total == 0:
                    st.error("Preencha o campo para atualizar os produtos!")
                else:
                    percentual = valor_reajuste_porcentagem_total / 100
                    Controle.Rejustar_Todos(percentual)
                    st.success("Produtos atualizados com sucesso!")






 