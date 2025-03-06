salario = float(input('Qual é o salário do funcionário? R$'))

nsalario = salario + (salario * 15 / 100)

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, ele vai receber R${nsalario :.2f}')