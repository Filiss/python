import random

aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')

alunos = [aluno1, aluno2, aluno3, aluno4]

lista = random.choice(alunos)

print(f'A ordem para a apresentação será: {lista}')