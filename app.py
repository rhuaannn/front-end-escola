import streamlit as st
from login.page import show_login
from professor.page import show_professor
from auxiliar.page import show_auxiliar
from intervalo.page import show_intervalo


def main():
    if 'token' not in st.session_state:
        show_login()

    else:
        st.title("Agendamentos")

        menu_option = st.sidebar.selectbox(
            "Cadastrar",
            ("Início", "Professor", "Auxiliar", "Intervalo")
        )
        if menu_option == 'Professor':
            show_professor()

        if menu_option == 'Auxiliar':
            show_auxiliar()
        
        if menu_option == 'Intervalo':
            show_intervalo()
            
            


if __name__ == '__main__':
    main()
