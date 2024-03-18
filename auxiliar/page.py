import pandas as pd
import streamlit as st
from auxiliar.service import AuxiliarService
from st_aggrid import AgGrid, ExcelExportMode


def show_auxiliar():
    auxiliar_service = AuxiliarService()
    auxiliar = auxiliar_service.get_auxiliar()

    if auxiliar:
        st.write('Lista de auxiliares:')
        auxiliar_df = pd.json_normalize(auxiliar)
        AgGrid(
            data=auxiliar_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='auxiliar_grid',
        )
    else:
        st.warning('Nenhum auxiliar encontrado.')

    st.title('Cadastrar Novo auxiliar')
    name = st.text_input('Nome do auxiliar')
    email = st.text_input('Email do auxiliar')
    if st.button('Cadastrar'):
        new_auxiliar = auxiliar_service.create_auxiliar(
            name=name,
            email=email,
        )
        if new_auxiliar:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o auxiliar. Verifique os campos')