import streamlit as st
from controle import Controle
import time

class Carrinho:
    def main():
        st.header("Adicionar Produto no Carrinho")
        produto = Controle.Produto_Listar()
        if len(produto) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Selecione o produto", produto)
            quantidade = st.number_input("Informe a quantidade: ", value=0, step=1, key="quantidade_1")
            if st.button("Adicionar"):
                if quantidade > op.estoque:
                    st.error("Estoque insuficiente")
                else:
                    for venda in Controle.Listar_Venda():
                        # id, data, carrinho, total, id_Cliente
                        # View.vendaItemInserir
                        # id, nome, qtd, preco, id_venda, id_produto


                        if venda.id_Cliente == st.session_state["clienteId"] and venda.carrinho == True:
                            Controle.Adicionar_VendaItem(op.descricao, quantidade, op.preco, venda.id, op.id)
                            Controle.Produto_Atualizar(op.id, op.descricao, op.preco, op.estoque - quantidade, op.id_categoria)
                            Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total + (op.preco  * quantidade), venda.id_Cliente)
                            st.success("Produto adicionado ao carrinho com sucesso!")
                            time.sleep(2)
                            st.rerun()