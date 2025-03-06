carro = int(input('Quanto tempo você ficou com o carro alugado?'))
km = float(input('Quantos km você rodou com o carro?'))

preco1 = carro * 60
preco2 = km * 0.15
total = preco1 + preco2

print(f'Com {carro} dias alugados e {km}km rodados, o preço total do aluguel é de R${total :.2f}')