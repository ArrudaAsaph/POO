import streamlit as st
from controle import Controle
import pandas as pd
from datetime import datetime
import time

class UI_Pedidos:
    def main():
        st.session_state.page = "pagina1"
        tab1, tab2= st.tabs(["Fechar Pedido", "Pedidos Realizados"])
        with tab1:
            UI_Pedidos.fecharPedido()
        with tab2:
            UI_Pedidos.pedidosRealizados()

    def fecharPedido():
        st.title("Fechar Pedido")
        vendas = Controle.Listar_Venda()
        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            with st.container(border=True):
                cliente = None
                for obj in Controle.Cliente_Listar():
                    if obj.id == st.session_state["clienteId"]:
                        cliente = obj

                venda = None
                for obj in vendas:
                    if obj.id_Cliente == st.session_state["clienteId"] and obj.carrinho == True:
                        venda = obj

                if venda == None:
                    st.write("Nenhum pedido ativo")
                else:
                    st.header(f"Fechar pedido {venda.id} de {cliente.nome}")
                    st.subheader(f"Total: R$ {venda.total:.2f}")
                    data = venda.data
                    data_obj = datetime.fromisoformat(data)
                    data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                    if venda.carrinho == True:
                        st.write(f"Carrinho Ativo - " + data_formatada)
                    else:
                        st.write("Carrinho Fechado - " + data_formatada)
                    if st.button("Fechar Pedido"):
                        if vendas[len(vendas) - 1].total == 0:
                            st.write("Nenhum pedido realizado")
                        else:
                            for venda in vendas:
                                venda.carrinho = (False)
                                Controle.Atualizar_Venda(venda.id, venda.data, venda.carrinho, venda.total, venda.id_Cliente)
                            Controle.Adicionar_Venda(True, 0, st.session_state["clienteId"])
                            st.success("Pedido fechado com sucesso!")
                            time.sleep(2)
                            st.rerun()

    def pedidosRealizados():
        st.header("Pedidos Realizados")
        vendas = []
        for venda in Controle.Listar_Venda():
            if venda.id_Cliente == st.session_state["clienteId"]:
                vendas.append(venda)

        cliente = None
        for obj in Controle.Cliente_Listar():
            if obj.id == st.session_state["clienteId"]:
                cliente = obj

        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            for i, venda in enumerate(vendas):
                with st.container(border=True):
                    st.header(f"Pedido {i} de {cliente.nome}")
                    st.subheader(f"Total: R$ {venda.total:.2f}")
                    data = venda.data
                    data_obj = datetime.fromisoformat(data)
                    data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                    if venda.carrinho == True:
                        st.write(f"Carrinho Ativo - " + data_formatada)
                    else:
                        st.write("Carrinho Fechado - " + data_formatada)

    @staticmethod    
    def visualizar_Pedidos():
        st.title("Todos os Pedidos")
        vendas = Controle.Listar_Venda()
        if len(vendas) == 0:
            st.write("Nenhum pedido realizado")
        else:
            for venda in Controle.Listar_Venda():
                for cliente in Controle.Cliente_Listar():
                    with st.container(border=True):
                        if venda.id_Cliente == cliente.id:
                            st.header(f"Pedido: {venda.id} de {cliente.nome}")
                            st.subheader(f"Total: R$ {venda.total:.2f}")
                            data = venda.data
                            data_obj = datetime.fromisoformat(data)
                            data_formatada = data_obj.strftime("dia: %d / %m / %Y às %H horas e %M minutos")
                            if venda.carrinho == True:
                                st.write(f"Carrinho Ativo - " + data_formatada)
                            else:
                                st.write("Carrinho Fechado - " + data_formatada)