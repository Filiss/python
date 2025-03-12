from random import randint

computador = randint(0, 5)
print('-¨' * 31)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar...')
print('-¨' * 31)

jogador = int(input('Em que número eu pensei?'))

if jogador == computador:
    print(f'Você acertou em qual número eu estava pensando, mas só dessa vez! Parabéns!')
else:
    print(f'Você errou o número que eu estava pensando! Você nunca vai conseguir adivinhar! Eu estava pensando no número {computador}! Boa sorte na próxima tentativa!')