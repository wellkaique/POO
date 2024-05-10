from Atividade4 import ContaBancaria
from Atividade4 import Cliente
cliente1 = Cliente("João", "Pessoa Física", "Rua ABC, 123", "123.456.789-00")
conta1 = ContaBancaria("Corrente", 1000)

print(f"Saldo atual: R${conta1.consultar_saldo()}")
conta1.depositar_valor(500)
print(f"Saldo atual: R${conta1.consultar_saldo()}")

conta1.mostrar_dados_cliente(cliente1.nome, cliente1.cpf)

conta1.encerrar_conta()

