import streamlit as st
from controle import Controle
import pandas as pd
import time

class UI_Carrinho:
    def main():
        # Verifica se clienteId está na sessão
        if "clienteId" not in st.session_state:
            st.error("Sessão inválida. Por favor, faça login novamente.")
            return
        
        # Divide as abas para interações
        tab1, tab2, tab3 = st.tabs(["Adicionar Produto", "Remover Produto Escolhido", "Atualizar Produto Escolhido"])
        with tab1:
            st.write(st.session_state["clienteId"])
            UI_Carrinho.adicionarProdutoNoCarrinho()
        with tab2:
            UI_Carrinho.removerProdutoNoCarrinho()
        with tab3:
            UI_Carrinho.atualizarProdutoNoCarrinho()
    
    

    @staticmethod
    def Listar_Carrinho():
        st.header("Itens no Carrinho")

        # Busca as vendas ativas do cliente
        vendas = Controle.Listar_Venda()
        venda_ativa = None
        for venda in vendas:
            if venda.id_Cliente == st.session_state.get("clienteId"):
                venda_ativa = venda
                break

        if not venda_ativa:
            st.write("Nenhuma venda ativa encontrada.")
            return

        # Lista os itens do carrinho para a venda ativa
        itens_carrinho = [
            item for item in Controle.Listar_VendaItem() if item.id_venda == venda_ativa.id
        ]

        if len(itens_carrinho) == 0:
            st.write("Nenhum item encontrado no carrinho.")
            return

        # Criação de DataFrame com os itens
        st.write("Tabela de Itens no Carrinho")
        dados_itens = [
            {
                "ID do Item": item.id,
                "Descrição": item.nome,
                "Quantidade": item.qtd,
                "Preço Unitário": item.preco,
                "Subtotal": item.qtd * item.preco,
            }
            for item in itens_carrinho
        ]
        df = pd.DataFrame(dados_itens)

        st.dataframe(df, use_container_width=True)

 

    def adicionarProdutoNoCarrinho():
        st.header("Adicionar Produto no Carrinho")
        produtos = Controle.Produto_Listar()
        for produto in produtos:
            if produto.estoque == 0:
                produtos.remove(produto)
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produtos, key="produto_1")
            quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_1")
            if st.button("Adicionar"):
                if quantidade <= 0:
                    st.error("Quantidade invalida")
                else:
                    if quantidade > op.estoque:
                        st.error("Estoque insuficiente")
                    else:
                        for venda in Controle.Listar_Venda():
                            # id, data, carrinho, total, id_Cliente
                            # id, nome, qtd, preco, id_venda, id_produto
                            if venda.id_Cliente == st.session_state["clienteId"] and venda.carrinho == True:
                                Controle.Adicionar_VendaItem(op.descricao, quantidade, op.preco, venda.id, op.id)
                                Controle.Produto_Atualizar(op.id, op.descricao, op.preco, op.estoque - quantidade, op.id_categoria)
                                Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)
                                st.success("Produto adicionado ao carrinho com sucesso!")
                                time.sleep(2)
                                st.rerun()
            
    def removerProdutoNoCarrinho():
        st.header("Remover Produto no Carrinho")

        vendas = Controle.Listar_Venda()
        venda = None
        for obj in vendas:
            if obj.id_Cliente == st.session_state["clienteId"] and obj.carrinho == True:
                venda = obj

        if venda is None:
            st.write("Nenhuma venda ativa encontrada.")
            return

        vendaItens = []
        for vendaitem in Controle.Listar_VendaItem():
            if vendaitem.id_venda == venda.id:
                vendaItens.append(vendaitem)
        
        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado no carrinho.")
        else:
            op = st.selectbox("Selecione o produto", vendaItens, key="produto_2")
            if st.button("Remover"):
                produto = None
                for obj in Controle.Produto_Listar():
                    if obj.id == op.id_produto:
                        produto = obj

                if produto is not None:
                    Controle.Excluir_VendaItem(op.id)
                    Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + vendaitem.qtd, produto.id_categoria)
                    Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total - (op.preco * op.qtd), venda.id_Cliente)
                    st.success("Produto removido do carrinho com sucesso!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Produto não encontrado.")

    def atualizarProdutoNoCarrinho():
        st.header("Atualizar Produto no Carrinho")

        vendas = Controle.Listar_Venda()
        venda = None
        for obj in vendas:
            if obj.id_Cliente == st.session_state["clienteId"] and obj.carrinho == True:
                venda = obj
                break  # Saia do loop ao encontrar a venda

        # Verifica se há uma venda ativa
        if venda is None:
            st.write("Nenhuma venda ativa encontrada.")
            return

        vendaItens = []
        for vendaitem in Controle.Listar_VendaItem():
            if vendaitem.id_venda == venda.id:
                vendaItens.append(vendaitem)

        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado no carrinho.")
            return

        op = st.selectbox("Selecione o produto", vendaItens, key="produto_3")
        quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_2")

        if st.button("Atualizar"):
            if quantidade <= 0:
                st.error("Quantidade inválida.")
                return

            # Localiza o produto correspondente
            produto = next((p for p in Controle.Produto_Listar() if p.id == op.id_produto), None)

            if produto is None:
                st.error("Produto não encontrado.")
                return

            # Verifica o estoque disponível
            if quantidade > produto.estoque:
                st.error("Estoque insuficiente.")
                return

            # Atualiza os dados
            Controle.Atualizar_VendaItem(op.id, op.nome, quantidade, op.preco, op.id_venda, op.id_produto)
            Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque - quantidade, produto.id_categoria)
            Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)

            st.success("Produto atualizado no carrinho com sucesso!")
            time.sleep(2)
            st.rerun()

            st.header("Atualizar Produto no Carrinho")

            vendas = Controle.Listar_Venda()
            venda = None
            for obj in vendas:
                if obj.id_Cliente == st.session_state["clienteId"] and obj.carrinho == True:
                    venda = obj

            # Verifica se há uma venda ativa
            if venda is None:
                st.write("Nenhuma venda ativa encontrada.")
                return

            vendaItens = []
            for vendaitem in Controle.Listar_VendaItem():
                if vendaitem.id_venda == venda.id:
                    vendaItens.append(vendaitem)
                    
            if len(vendaItens) == 0:
                st.write("Nenhum produto cadastrado")
                return
            else:
                op = st.selectbox("Selecione o produto", vendaItens, key="produto_3")
                quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_2")
                if st.button("Atualizar"):
                    if quantidade <= 0:
                        st.error("Quantidade invalida")
                    else:
                        produto = None
                        for obj in Controle.Produto_Listar():
                            if obj.id == op.id_produto:
                                produto = obj
                        
                        Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + op.estoque, produto.id_categoria)
                        Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)

                        for obj in Controle.Produto_Listar():
                            if obj.id == op.id_produto:
                                produto = obj

                        if quantidade > produto.estoque:
                            st.error("Estoque insuficiente")
                        else:
                            Controle.Atualizar_VendaItem(op.id, op.nome, quantidade, op.preco, op.id_venda, op.id_produto)
                            Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + op.estoque, produto.id_categoria)

                            Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)
                            st.success("Produto atualizado no carrinho com sucesso!")
                            time.sleep(2)
                            st.rerun()

                st.header("Atualizar Produto no Carrinho")

                vendas = Controle.Listar_Venda()
                venda = None
                for obj in vendas:
                    if obj.id == st.session_state["clienteId"] and obj.carrinho == True:
                        venda = obj

                vendaItens = []
                for vendaitem in Controle.Listar_VendaItem():
                    st.write(vendaitem)
                    if vendaitem.id_venda == venda.id:
                        vendaItens.append(vendaitem)
                    
                if len(vendaItens) == 0:
                    st.write("Nenhum produto cadastrado")
                else:
                    op = st.selectbox("Selecione o produto", vendaItens, key="produto_3")
                    quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_2")
                    if st.button("Atualizar"):
                        if quantidade <= 0:
                            st.error("Quantidade invalida")
                        else:
                            produto = None
                            for obj in Controle.Produto_Listar():
                                if obj.id == op.id_produto:
                                    produto = obj
                            
                            
                            Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + op.estoque, produto.id_categoria)
                            Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)

                            for obj in Controle.Produto_Listar():
                                if obj.id == op.id_produto:
                                    produto = obj

                            if quantidade > produto.estoque:
                                st.error("Estoque insuficiente")
                            else:
                                Controle.Atualizar_VendaItem(op.id, op.nome, quantidade, op.preco, op.id_venda, op.id_produto)
                                Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + op.estoque, produto.id_categoria)

                                Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)
                                st.success("Produto atualizado no carrinho com sucesso!")
                                time.sleep(2)
                                st.rerun()