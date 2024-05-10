class Teste:
    def __init__(self,valor):
        self.__valor = valor



    @property
    def get_valor(self):
        return self.__valor
    # um traço =  visibilidade protegida / dois traços =  visibilidade privada
    # metodo para buscar e mostrar o valor


    @valor.setter
    def set_valor(self,valor):
        print(valor)
        self.__valor = valor
        #metodo para alterar o valor