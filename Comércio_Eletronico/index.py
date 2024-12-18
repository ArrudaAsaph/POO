import streamlit as st
from templates.class_Cadastro import UI_Cadastro
from templates.class_Login import UI_Login
from templates.class_listaClientes import UI_Clientes

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
        UI_Clientes.main()
        
        

    def Usuario_Tela():
        st.write("Seja bem-vindo Usuário!")
        

# Index.Main()
UI_Clientes.main()