#Criando a classe pessoa
class Pessoa:
    def __init__(self, nome=str, data_nasc=str, matricula=int):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__matricula = matricula
#metodo para acessar o atributo nome
    def get_nome(self):
        return self.__nome
#metodo set para caso seja necessario alterar o nome
    def set_nome(self, nome):
        self.__nome = nome
#metodo para acessar o valor data de nascimento
    def get_data_nasc(self):
        return self.__data_nasc
# metodo para modificar a data de nascimento
    def set_data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc

#metodo get para acessar o valor da matricula
    def get_matricula(self):
        return self.__matricula

#metodo get para acessar a matrícula

    def set_matricula(self, matricula):
        self.__matricula = matricula

#Classe professor e seus atributos
class Professor(Pessoa):
    professores_cadastrados = []

    def __init__(self, nome=str, data_nasc=str, matricula=int, disciplina=str, turno=str):
        super().__init__(nome, data_nasc, matricula)
        self.__disciplina = disciplina
        self.__turno = turno
        Professor.professores_cadastrados.append(self)
#metodo para acessar a disciplina
    def get_disciplina(self):
        return self.__disciplina
#metodo para alterar a disciplina
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
#metodo para acessar o turno
    def get_turno(self):
        return self.__turno
#metodo para alterar o turno
    def set_turno(self, turno):
        self.__turno = turno
#metodo para mostrar as informações do professor
    def info_prof(self):
        print(f'Nome:{self.get_nome()}\nData de nascimento:{self.get_data_nasc()}\nMatricula:{self.get_matricula()}')
#metodo estatico para receber o nome do professor e adiciona-los a uma lista
    @staticmethod
    def listar_professores():
        return [professor.get_nome() for professor in Professor.professores_cadastrados]

#Classe Pessoa , praticamente a mesmas informações da classe professor
class aluno(Pessoa):
    alunos_cadastrados = []

    def __init__(self, nome=str, data_nasc=str, matricula=int, doc=int):
        super().__init__(nome, data_nasc, matricula)
        self.__doc = doc
        aluno.alunos_cadastrados.append(self)

    def get_doc(self):
        return self.__doc

    def set_doc(self, doc):
        self.__doc = doc

    @staticmethod
    def listar_alunos():
        return [aluno.get_nome() for aluno in aluno.alunos_cadastrados]


class Curso:
    def __init__(self, id=int, nome=str, periodo=str):
        self.__id = id
        self.__nome = nome
        self.__periodo = periodo
        self.__prof = None

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_periodo(self):
        return self.__periodo

    def set_periodo(self, periodo):
        self.__periodo = periodo

    def get_prof(self):
        return self.__prof

    def set_prof(self, prof):
        self.__prof = prof

    def insere_prof(self, prof):
        self.__prof = prof

    def curso_prof(self):
        if self.__prof:
            return f'Curso: {self.__nome}, Período: {self.__periodo}, Professor: {self.__prof.get_nome()}'
        else:
            return f'Curso: {self.__nome}, Período: {self.__periodo}, Professor: Não atribuído'

