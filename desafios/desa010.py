preço = float(input('Qual é o preço do produto? R$'))

npreço = preço - (preço * 5 / 100)

print(f'O preço do produto que custava R${preço}, com 5% de desconto, ele vai custar R${npreço :.2f}')
