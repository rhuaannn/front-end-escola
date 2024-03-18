import pandas as pd
import streamlit as st
from intervalo.service import IntervaloService
from st_aggrid import AgGrid, ExcelExportMode
from datetime import datetime, time

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

    # Solicitar data e hora para o horário de entrada
    entrada_date = st.date_input('Data do horário de entrada')
    entrada_time = st.time_input('Horário de entrada', time(8, 0))  # Padrão para 08:00
    entrada = datetime.combine(entrada_date, entrada_time)

    # Solicitar data e hora para o horário do almoço
    almoco_date = st.date_input('Data do horário do almoço')
    almoco_time = st.time_input('Horário do almoço', time(12, 0))  # Padrão para 12:00
    almoco = datetime.combine(almoco_date, almoco_time)

    # Solicitar data e hora para o retorno do almoço
    retorno_almoco_date = st.date_input('Data do retorno do almoço')
    retorno_almoco_time = st.time_input('Horário do retorno do almoço', time(13, 0))  # Padrão para 13:00
    retorno_almoco = datetime.combine(retorno_almoco_date, retorno_almoco_time)

    # Solicitar data e hora para a saída do expediente
    saida_expediente_date = st.date_input('Data da saída do expediente')
    saida_expediente_time = st.time_input('Horário da saída do expediente', time(17, 0))  # Padrão para 17:00
    saida_expediente = datetime.combine(saida_expediente_date, saida_expediente_time)

    descricao = st.text_area('Descrição do intervalo')

    if st.button('Cadastrar'):
        new_intervalo = intervalo_service.create_intervalo(
            name=name,
            name_auxiliar=name_auxiliar,
            entrada=entrada,
            almoco=almoco,
            retorno_almoco=retorno_almoco,
            saida_expediente=saida_expediente,
            descricao=descricao
        )
        if new_intervalo:
            st.success('Intervalo cadastrado com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao cadastrar o Intervalo. Verifique os campos')
