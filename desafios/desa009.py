largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura}, sua área é de {area}m² e você precisará de {tinta}l de tinta para pintá-la.')