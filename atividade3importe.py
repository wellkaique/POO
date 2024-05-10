from atividade3 import ContaBancaria
minha_conta1 = ContaBancaria("João", "corrente", "1000", True)

# Consultando o saldo
saldo_atual = minha_conta1.consultar_saldo()
print("Saldo atual:", saldo_atual)

# Depositando um valor
minha_conta1.depositar_valor(500.0)
print("Saldo após o depósito:", minha_conta1.consultar_saldo())

#Sacar um valor
minha_conta1.sacar_valor(500.0)
print("Saldo após o depósito:", minha_conta1.sacar_valor(200.00))

#sair da conta
minha_conta1.sair_da_conta()

#encerrar a conta
minha_conta1.encerrar_conta()


