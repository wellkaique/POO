"""Crie uma classe Cliente que terá os seguintes atributos: Nome, tipo de
cliente: comum ou especial, Endereço, cpf, crie um método que mostre
os dados do cliente
2. Crie uma classe que se chama ContaBancaria com os seguintes
atributos: Numero da conta,Tipo de conta que poderá ser (CC ou CP) e
saldo. Esta classe poderá ter os seguintes métodos :Mostrar Dados do
conta junto com o nome e o cpf do cliente(),Mostrar Operações que é
possível fazer com a conta: Consultar saldo, depositar valor, sacar valor,
sair da conta e encerrar conta.
Vale salientar que para depositar um valor na conta ela precisa estar
com status ativo, caso contrário não será possível depositar.
Para fazer a operação de saque o cliente precisa ter saldo, senão tiver o
dinheiro não poderá ser sacado e para encerrar uma conta o saldo da
conta precisa estar zerado.

Obs: Não esqueça de trabalhar com encapsulamento."""
import random

class Cliente:
    def __init__(self, nome: str, tipo: str, endereco: str, cpf: str) -> object:
        self.nome = nome
        self.tipo = tipo
        self.endereco = endereco
        self.cpf = cpf


class ContaBancaria:
    def __init__(self, tipo: str, saldo: float):
        self.numerodaconta = self.gerar_numero_conta()
        self.tipo = tipo
        self.saldo = saldo
        self.status = "Ativa"

    def gerar_numero_conta(self):
        return str(random.randint(1000, 9999))

    def consultar_saldo(self):
        return self.saldo

    def depositar_valor(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sair_da_conta(self):
        print("Você saiu da sua conta.")

    def encerrar_conta(self):
        if self.saldo == 0:
            self.status = "Encerrada"
            print("Sua conta foi encerrada com sucesso.")
        else:
            print("Sua conta precisa estar zerada para ser encerrada.")


    def mostrar_dados_cliente(self, nome,cpf):
        print(f"Dados do cliente: ")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
