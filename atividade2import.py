from atividade2 import BombaCombustivel
bomba = BombaCombustivel("Gasolina",5.0, 1000,  1500)

litros_abastecidos = bomba.abastecerPorValor(50)
print("Litros abastecidos:",litros_abastecidos)

valor_a_pagar = bomba.abastecerPorLitro(20)
print("Valor a pagar:",valor_a_pagar)

bomba.alterarValor(5.5)
bomba.alterarCombustivel("Diesel")
bomba.alterarQuantidadeCombustivel(1500)
