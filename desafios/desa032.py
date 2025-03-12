viagem  = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {viagem:.1f}Km.')
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(f'E o preço da sua viagem será de {preco:.2f}R$')