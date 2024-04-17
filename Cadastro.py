from typing import Any


class Aluno:
    # nome = str
    # __cpf = str
    # email = str

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.__cpf = cpf
        self.email = email

    def getcpf(self):
        return self.__cpf

    def setcpf(self, cpf):
        self.__cpf = cpf


# Aluno.__init__(Aluno, "pedro", 2525, "pedro2")
# print(Aluno.getcpf(Aluno))
# Aluno.setcpf(Aluno, 2548)
# print(Aluno.getcpf(Aluno))

class Professor:
    # nome = str
    # __cpf = str
    # email = str
    # __contrato = str

    def __init__(self, nome, cpf, email, contrato):
        self.nome = nome
        self.__cpf = cpf
        self.email = email
        self.__contrato = contrato

    def getcpf(self):
        return self.__cpf

    def setcpf(self, cpf):
        self.__cpf = cpf

    def getcontrato(self):
        return self.__contrato

    def setcontrato(self, contrato):
        self.__contrato = contrato


class Disciplina:
    # nomeDisciplina = str
    # professorDisciplina = Professor
    # alunosDisciplina = Aluno

    def __init__(self, nomeDisciplina, professorDisciplina, alunosDisciplina):
        self.nomeDisciplina = nomeDisciplina
        self.professorDisciplina = professorDisciplina
        self.alunosDisciplina = alunosDisciplina


class Sala:
    # numeroSala = int

    def __init__(self, numeroSala):
        self.numeroSala = numeroSala


class Endereco:
    # cep = str
    # logradouro = str
    # cidade = str
    def __init__(self, cidade, cep, logradouro):
        self.cidade = cidade
        self.cep = cep
        self.logradouro = logradouro


class Curso:

    def __init__(self):
        self.alunos = []

    def cadastrarAluno(self, nome, cpf, email):
        aluno = Aluno(nome, cpf, email)
        self.alunos.append(aluno)

    def mostrarAlunos(self):
        for aluno in self.alunos:
            print(aluno)


# curso = Curso()
# curso.cadastrarAluno("Marcelo", 2525, "marcelob@example.com")
# curso.cadastrarAluno("Carla", 1111, "carla@example.com")

# curso.mostrarAlunos()
