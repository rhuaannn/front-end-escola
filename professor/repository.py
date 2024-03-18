import requests
import streamlit as st
 

class ProfessorRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/'
        self.__genres_url = f'{self.__base_url}professor/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_professor(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_professor(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
         