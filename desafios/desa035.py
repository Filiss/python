salario = float(input('Digite o salário do funcionário: R$'))

if salario <= 1250:
    salariob = salario + (salario * 15 / 100)
else:
    salariob = salario + (salario * 10 / 100)

print(f'O salário do funcionário que era R${salario} passa a ser R${salariob :.2f}.')