from atividadeavaliacao01 import Professor
from atividadeavaliacao01 import aluno
from atividadeavaliacao01 import Curso


professor1 = Professor("Raquel", "dd/mm/aaaa", 123, "POO", "Manhã")
professor2 = Professor("Geyder", "dd/mm/aaaa", 456, "BD", "Manhã")

aluno1 = aluno("Kaique", "04/07/1996", 222, 34565895)
aluno2 = aluno("wellington", "05/07/1996", 654, 987654321)

curso1 = Curso(1, "POO", "Manhã")
curso2 = Curso(2, "BD", "Noite")

curso1.set_prof(professor1)
curso2.set_prof(professor2)

print(' Professor 1: ')
professor1.info_prof()

print("\nInformações dos Cursos e Professores: ")
print(curso1.curso_prof())
print(curso2.curso_prof())

print("\nProfessores Cadastrados: ")
lista_professores = Professor.listar_professores()
for professor in lista_professores:
    print(professor)

print("\nAlunos Cadastrados: ")
lista_alunos = aluno.listar_alunos()
for aluno in lista_alunos:
    print(aluno)