import requests
import streamlit as st
import requests


class ProfessorRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/'
        self.__professor_url = f'{self.__base_url}professor/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_professor(self):
        response = requests.get(
            self.__professor_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:

            return None
        raise Exception(f'Erro ao obter dados da API.{response.status_code}')

    def create_professor(self, professor, auxiliar):
        response = requests.post(
            self.__professor_url,
            headers=self.__headers,
            data=dict(professor, auxiliar)
        )
        if response.status_code == 201:
            return response.json()
