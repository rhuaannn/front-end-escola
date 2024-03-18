import requests
import streamlit as st

import requests


class AuxiliarRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/'
        self.__auxiliar_url = f'{self.__base_url}auxiliar/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_auxiliar(self):
        response = requests.get(
            self.__auxiliar_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:

            return None
        raise Exception(
            f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_auxiliar(self, auxiliar):
        response = requests.post(
            self.__auxiliar_url,
            headers=self.__headers,
            data=auxiliar,
        )
        if response.status_code == 201:
            return response.json()
