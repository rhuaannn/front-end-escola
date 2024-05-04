import requests
from intervalo.repository import IntervaloRepository


class IntervaloService:
    def __init__(self):
        self.intervalo_repository = IntervaloRepository()

    def get_intervalo(self):
        return self.intervalo_repository.get_intervalo()

    def create_intervalo(self, entrada, almoco, retorno_almoco, saida_expediente, descricao, professor):
        # Construir o payload para o POST
        payload = {

            "entrada": entrada.strftime('%Y-%m-%dT%H:%M:%S'),
            "almoco": almoco.strftime('%Y-%m-%dT%H:%M:%S'),
            "retorno_almoco": retorno_almoco.strftime('%Y-%m-%dT%H:%M:%S'),
            "saida_expediente": saida_expediente.strftime('%Y-%m-%dT%H:%M:%S'),
            "descricao": descricao,
            "professor": {
                "name": professor
            }

        }
        print(payload)
        return self.intervalo_repository.create_intervalo(payload)
