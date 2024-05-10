class BombaCombustivel:
    def __init__(self, tipo, valor, litro, quantidade):
        self.tipo = tipo
        self.valor = valor
        self.litro = litro
        self.quantidade = quantidade

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valor
        if litros_abastecidos > self.quantidade:
            print("Desculpe, não há combustível suficiente.")
        else:
            self.quantidade -= litros_abastecidos
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valor
        if litros > self.quantidade:
            print("Desculpe, não há combustível suficiente.")
        else:
            self.quantidade -= litros
            print(f"O valor a pagar é R${valor_a_pagar:.2f}.")

    def alterarValor(self, novo_valor):
        self.valor = novo_valor
        print(f"O valor do litro de {self.tipo} foi alterado para R${novo_valor:.2f}.")

    def alterarCombustivel(self, novo_tipo):
        self.tipo = novo_tipo
        print(f"O tipo de combustível foi alterado para {novo_tipo}.")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade = nova_quantidade
        print(f"A quantidade de combustível foi alterada para {nova_quantidade} litros.")
