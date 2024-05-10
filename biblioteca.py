class Livro:
    def __int__(self, titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f"Veículo: {self.titulo} {self.autor}, ano : {self.ano}"

    def emprestar(self):
        self.disponivel = False



    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [
            Livro("Dom casmurro", "Machado de Assis," 1899)
        Livro("Dom casmurro", "Machado de Assis,"1899)
        Livro("Dom casmurro", "Machado de Assis,"1899)
        ]
        return [livro from li]