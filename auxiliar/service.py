from auxiliar.repository import AuxiliarRepository


class AuxiliarService:

    def __init__(self):
        self.auxiliar_repository = AuxiliarRepository()

    def get_auxiliar(self):
        return self.auxiliar_repository .get_auxiliar()

    def create_auxiliar(self, name, email):
        auxiliar = dict(
            name=name,
            email=email,
        )
        return self.auxiliar_repository .create_auxiliar(auxiliar)