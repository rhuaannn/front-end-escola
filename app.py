import streamlit as st
from login.page import show_login


def main():
    if 'token' not in st.session_state:
        show_login()

    else:
        st.title("Agendamentos")

        st.sidebar.selectbox(
            "Cadastrar",
            ("Professor", "Auxiliar", "Intervalo")
        )

if __name__ == '__main__':
    main()
