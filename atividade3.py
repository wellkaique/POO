import random
class ContaBancaria:
    """metodo construtor para a classe conta bancaria """
    def __init__(self, nome, tipo, saldo,status="Ativa"):
        self.nome = nome
        self.tipo = tipo
        self.saldo = float(saldo)
        self.status = True

    def gerar_numero_conta(self):
        return str(random.randint(0o01, 100))


    def mostrar_dados(self):
        """função para mostrar os dados da conta """
        print("Nome:", self.nome)
        print("Número da conta:", self.numeroconta)
        print("Tipo:", self.tipo)
        print("Saldo:", self.saldo)

    def consultar_saldo(self):
        return self.saldo

    def depositar_valor(self, valor_depositado):
        if valor_depositado > 0:
            self.saldo += valor_depositado
            print("Depósito de R${:.2f} realizado com sucesso.".format(valor_depositado))
        else:
            print("O valor do depósito deve ser superior a 0.")

    def sacar_valor(self, valor_saque):
        if valor_saque > 0:
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque
                print("Saque de R${:.2f} realizado com sucesso.".format(valor_saque))
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser superior a 0.")

    def sair_da_conta(self):
        print("Você saiu da sua conta")



    def encerrar_conta(self):
        print("Sua conta foi encerrada")

