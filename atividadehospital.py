class Hospital:
    def __init__(self,nome: str, CNPJ: int):
        self.nome = nome
        self.CNPJ = CNPJ
        self.alas = []

class Enfermeira:
    def __init__(self, CRE: int):
        self.nome_enfermeiro = []
        self.CRE = CRE
        self.enfermeiro_chefe = []

class Medico:
    def __init__(self,nome:str, CRM: int, especialidade: str):
        self.nome = []
        self.CRM = CRM
        self.especialidade = especialidade

class planosaude:
    def __init__(self, nome: str, telefone_operadora: str):
        self.nome = nome
        self.telefone_operadora = telefone_operadora
        self.medicos_credenciados = []

    def add_medicos_credenciados(self,medico: Medico):
        self.medicos_credenciados(medico)

class Ala:
    def __init__(self, identificador: int, enfermeira_responsavel: Enfermeira):
        self.identificador = identificador
        self.enfermeira_responsavel = enfermeira_responsavel



    def adicionar_ala(self, ala: Ala):
        self.alas.append(ala)

    def credenciar_plano(self, plano: PlanoSaude):
        self.plano = plano

    def registrar_atendimento(self,paciente: str, medico: Medico, data: str, hora: str):

        pass







