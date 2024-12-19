import streamlit as st
from controle import Controle
import time

class UI_Carrinho:
    def main():
        
        # st.session_state.page = "pagina1";
        tab1, tab2, tab3 = st.tabs(["Adicionar Produto", "Remover Produto Escolhido", "Atualizar Produto Escolhido"])
        with tab1:
            UI_Carrinho.adicionarProdutoNoCarrinho()
        with tab2:
            UI_Carrinho.removerProdutoNoCarrinho()
        with tab3:
            UI_Carrinho.atualizarProdutoNoCarrinho()

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
                            if venda.id == st.session_state["clienteId"] and venda.carrinho == True:
                                Controle.Adicionar_VendaItem(op.nome, quantidade, op.preco, venda.id, op.id)
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
            if obj.id == st.session_state["clienteId"] and obj.carrinho == True:
                venda = obj

        vendaItens = []
        for vendaitem in Controle.Listar_VendaItem():
            if vendaitem.id_venda == venda.id:
                vendaItens.append(vendaitem)
            
        if len(vendaItens) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", vendaItens, key="produto_2")
            if st.button("Remover"):
                produto = None
                for obj in Controle.Produto_Listar():
                    if obj.id == op.id_produto:
                        produto = obj

                Controle.Excluir_VendaItem(op.id)
                Controle.Produto_Atualizar(produto.id, produto.descricao, produto.preco, produto.estoque + op.estoque, produto.id_categoria)
                Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco * quantidade), venda.id_Cliente)
                st.success("Produto removido do carrinho com sucesso!")
                time.sleep(2)
                st.rerun()

    def atualizarProdutoNoCarrinho():
        st.header("Atualizar Produto no Carrinho")

        vendas = Controle.Listar_Venda()
        venda = None
        for obj in vendas:
            if obj.id == st.session_state["clienteId"] and obj.carrinho == True:
                venda = obj

        vendaItens = []
        for vendaitem in Controle.Listar_VendaItem():
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