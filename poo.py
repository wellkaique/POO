class Pessoa:
    #Crie uma classe que modele uma pessoa:
    #Atributos: nome, idade, peso, altura e sexo
    #Métodos: Envelhercer,  Calcular IMC, Crescer.
    #Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    #sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
        def __init__ (self, nome, idade,peso, altura, sexo):
           self.nome = nome
           self.idade = idade
           self.peso = peso
           self.altura = altura
           self.sexo = sexo


        def Envelhecer(self,anos=1):
            self.idade += anos
            if self.idade < 21:
            self.crescer(0.5 * anos)

        def calcular_IMC(self,):
            return self.peso / (self.altura ** 2)


        def crescer(self,cm):
            self.altura
