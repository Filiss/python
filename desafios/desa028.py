nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome sendo {nome}.')
print(f'Seu primeiro nome é: {nome.split()[0]}')
print(f'Seu último nome é: {nome.split()[-1]}')