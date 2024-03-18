import streamlit as st
from login.page import show_login
from professor.page import show_professor


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
        
if __name__ == '__main__':
    main()
