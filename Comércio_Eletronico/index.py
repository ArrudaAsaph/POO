import streamlit as st
from templates.class_Cadastro import UI_Cadastro
from templates.class_Login import UI_Login
from templates.class_UIClientes import UI_Clientes
from templates.class_UICategorias import UI_Categorias
from templates.class_UIProdutos import UI_Produtos
from templates.class_UICarrinho import UI_Carrinho
from templates.class_UIPedidos import UI_Pedidos

from controle import Controle

class Index:
    def Main():
        Index.Inicio()

    def Cadastro():
        UI_Cadastro.main()

    def Login():
        pessoa = UI_Login.main()  
        if pessoa == "admin":
            Index.Mudar_Page('admin')
            st.rerun()
        elif pessoa == "usuario":
            Index.Mudar_Page('usuario')
            st.rerun()

    @staticmethod
    def Mudar_Page(pagina):
        st.session_state.page = pagina

    def Inicio():
        if 'page' not in st.session_state:
            st.session_state.page = 'home'
        
        if st.session_state.page == 'home':
            st.write("Página Inicial")
            col1, col2 = st.columns(2)
            with col1:
                st.button("Entrar", on_click=lambda: Index.Mudar_Page('login'))
            with col2:
                st.button("Cadastro", on_click=lambda: Index.Mudar_Page('cadastro'))

        elif st.session_state.page == 'login':
            Index.Login()
            st.button("Voltar", on_click=lambda: Index.Mudar_Page('home'))
        
        elif st.session_state.page == 'cadastro':
            Index.Cadastro()
            st.button("Voltar", on_click=lambda: Index.Mudar_Page('home'))
        
        
        elif st.session_state.page == 'admin':
            Index.Admin_Tela()
            

        
       
        elif st.session_state.page == 'usuario':
            Index.Usuario_Tela()

    def Admin_Tela():
        st.write("Seja bem-vindo Admin!")
        op = st.sidebar.selectbox("Menu", ["Clientes", "Categorias", "Produtos", "Visualizar Pedidos"])
        if op == "Clientes":
            UI_Clientes.main()
        elif op == "Categorias":
            UI_Categorias.main()
        elif op == "Produtos":
            UI_Produtos.main()
        
        

    def Usuario_Tela():
        Controle.Adicionar_Venda(True, 0, st.session_state["clienteId"])
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar / Remover Produto no Carrinho", "Fechar Pedido", "Ver Meus Pedidos"])
        if op == "Listar Produtos":
            UI_Carrinho.Listar_Carrinho()
        if op == "Adicionar / Remover Produto no Carrinho":
            UI_Carrinho.main()
        if op == "Fechar Pedido":
            UI_Pedidos.fecharPedido()
        if op == "Ver Meus Pedidos":
            UI_Pedidos.visualizar_Pedidos()

    # def sairDoSistema():
    #     if st.sidebar.button("Sair"):
    #         View.vendaFechar(st.session_state["clienteId"])
    #         del st.session_state["clienteId"]
    #         del st.session_state["clienteNome"]
    #         st.rerun()

        

Index.Main()

# UI_Clientes.main()
# UI_Produtos.main()
# UI_Produtos.Reajuste()
# UI_Carrinho.main()