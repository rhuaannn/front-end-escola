from intervalo.repository import IntervaloRepository

class IntervaloService:

    def __init__(self):
        self.intervalo_repository = IntervaloRepository()

    def get_intervalo(self):
        return self.intervalo_repository.get_intervalo()

    def create_intervalo(self, name, name_auxiliar, entrada_data_hora, almoco_data_hora, retorno_almoco_data_hora, expediente_data_hora, descricao):
        intervalo = {

            'entrada': entrada_data_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'almoco': almoco_data_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'retorno_almoco': retorno_almoco_data_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'saida_expediente': expediente_data_hora.strftime('%Y-%m-%dT%H:%M:%S'),
            'descricao': descricao,
            'professor': name,
            'auxiliar': name_auxiliar
        }
        print (intervalo)
        return self.intervalo_repository.create_intervalo(intervalo)
        