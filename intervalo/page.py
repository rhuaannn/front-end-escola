import pandas as pd
import streamlit as st
from intervalo.service import IntervaloService
from st_aggrid import AgGrid, ExcelExportMode
from datetime import datetime


def show_intervalo():
    intervalo_service = IntervaloService()
    intervalo = intervalo_service.get_intervalo()

    if intervalo:
        st.write('Lista de Intervalos:')
        intervalo_df = pd.json_normalize(intervalo)
        AgGrid(
            data=intervalo_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='intervalo_grid',
        )
    else:
        st.warning('Nenhum intervalo encontrado.')

    st.title('Cadastrar Novo Intervalo')
    name = st.text_input('Nome do professor')
    name_auxiliar = st.text_input('Nome do Auxiliar')

    entrada = st.date_input('Data de entrada')
    entrada_hora = st.time_input('Hora da entrada')
    entrada_data_hora = datetime.combine(entrada, entrada_hora)

    almoco = st.date_input('Data do almoço')
    almoco_hora = st.time_input('Hora do almoço')
    almoco_data_hora = datetime.combine(almoco, almoco_hora)

    retorno_almoco = st.date_input('Data do retorno almoco')
    retorno_almoco_hora = st.time_input('Hora do retorno almoco')
    retorno_almoco_data_hora = datetime.combine(
        retorno_almoco, retorno_almoco_hora)

    expediente = st.date_input('Data do fim do expediente')
    expediente_hora = st.time_input('Hora do fim do expediente')
    expediente_data_hora = datetime.combine(expediente, expediente_hora)

    descricao = st.text_area('Descrição do intervalo')

    if st.button('Cadastrar'):
        new_intervalo = intervalo_service.create_intervalo(
            name=name,
            name_auxiliar=name_auxiliar,
            entrada_data_hora=entrada_data_hora,
            almoco_data_hora=almoco_data_hora,
            retorno_almoco_data_hora=retorno_almoco_data_hora,
            expediente_data_hora=expediente_data_hora,
            descricao=descricao
        )
        if new_intervalo:
            st.success('Intervalo cadastrado com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao cadastrar o Intervalo. Verifique os campos')
