# Definindo a classe pai (superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass  # Método a ser implementado pelas subclasses


# Definindo uma classe filha (subclasse) que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"


# Definindo outra classe filha (subclasse) que herda de Animal
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


# Criando instâncias das subclasses
cachorro1 = Cachorro("Bolinha")
gato1 = Gato("Whiskers")

# Chamando métodos das subclasses
print(cachorro1.nome + " faz " + cachorro1.fazer_som())
print(gato1.nome + " faz " + gato1.fazer_som())
