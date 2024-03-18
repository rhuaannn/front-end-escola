from professor.repository import ProfessorRepository


class ProfessorService:

    def __init__(self):
        self.professor_repository = ProfessorRepository()

    def get_professor(self):
        return self.professor_repository .get_professor()

    def create_professor(self, name, email):
        professor = dict(
            name=name,
            email=email,
        )
        return self.professor_repository .create_professor(professor)