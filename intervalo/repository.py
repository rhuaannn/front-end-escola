import requests
import streamlit as st

class IntervaloRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/'
        self.__intervalo_url = f'{self.__base_url}intervalo/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_intervalo(self):
        response = requests.get(
            self.__intervalo_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_intervalo(self, intervalo):
        response = requests.post(
            self.__intervalo_url,
            headers=self.__headers,
            json=intervalo,  # Alterado de data para json para garantir o tipo de conteúdo correto
        )
        if response.status_code == 201:
            return response.json()
        else:
            # Registro de erro adicionado
            mensagem_erro = f'Falha ao criar intervalo: {response.status_code}, Resposta: {response.text}'
            raise Exception(mensagem_erro)
