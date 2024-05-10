class Pessoa:
    # Crie uma classe que modele uma pessoa:
    # Atributos: nome, idade, peso, altura e sexo
    # Métodos: Envelhecer, Calcular IMC, Crescer.
    # Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    # sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def Envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def calcular_IMC(self, ):
         imc = self.peso / (self.altura ** 2)
         return round(imc,2)


    def crescer(self, cm):
        self.altura += cm


    def mostrar_informações(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Peso: ",self.peso)
        print("Altura: ",self.altura)
        print("Sexo: ", self.sexo)
        print("IMC:", self.calcular_IMC())