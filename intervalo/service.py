from intervalo.repository import IntervaloRepository


class IntervaloService:

    def __init__(self):
        self.intervalo_repository = IntervaloRepository()

    def get_intervalo(self):
        return self.intervalo_repository .get_intervalo()

    def create_intervalo(self, name, name_auxiliar, entrada, almoco, retorno_almoco, saida_expediente, descricao):
        intervalo = dict(
            name=name,
            name_auxiliar=name_auxiliar,
            entrada=entrada,
            almoco=almoco,
            retorno_almoco=retorno_almoco,
            saida_expediente=saida_expediente,
            descricao=descricao
        )
        return self.intervalo_repository .create_intervalo(intervalo)
