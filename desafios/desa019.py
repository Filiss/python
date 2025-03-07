
alunos1 = input('Digite o nome do primeiro aluno: ')
alunos2 = input('Digite o nome do segundo aluno: ')
alunos3 = input('Digite o nome do terceiro aluno: ')
alunos4 = input('Digite o nome do quarto aluno: ')

alunos = [alunos1, alunos2, alunos3, alunos4]
import random
random.shuffle(alunos)

print(f'O aluno escolhido foi o(a): {alunos[0]}')

