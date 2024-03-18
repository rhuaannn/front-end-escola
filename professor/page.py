import pandas as pd
import streamlit as st
from professor.service import ProfessorService
from st_aggrid import AgGrid, ExcelExportMode


def show_professor():
    professor_service = ProfessorService()
    professor = professor_service.get_professor()

    if professor:
        st.write('Lista de Professores:')
        professor_df = pd.json_normalize(professor)
        AgGrid(
            data=professor_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='professor_grid',
        )
    else:
        st.warning('Nenhum professor encontrado.')

    st.title('Cadastrar Novo Professor')
    name = st.text_input('Nome do Professor')
    email = st.text_input('Email do Professor')
    if st.button('Cadastrar'):
        new_professor = professor_service.create_professor(
            name=name,
            email=email,
        )
        if new_professor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o Professor. Verifique os campos')