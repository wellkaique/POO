from atividade1 import Pessoa
pessoa1 = Pessoa("Ana", 18,55,1.65, "Feminino")
print("Antes de envelhecer:", pessoa1.altura)
pessoa1.Envelhecer()
print("Depois de envelhecer:", pessoa1.altura)
print("IMC:", pessoa1.calcular_IMC())
pessoa1.mostrar_informações()