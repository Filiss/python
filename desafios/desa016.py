import math

valora = float(input('Digite o valor do A:'))
valorb = float(input('Digite o valor do B:'))
valorc = float(input('Digite o valor do C:'))

delta = valorb**2 - 4*valora*valorc
if delta < 0:
	raizdelta = None
	x1 = None
	x2 = None
else:
	raizdelta = math.sqrt(delta)
	x1 = (-valorb + raizdelta) / (2*valora)
	x2 = (-valorb - raizdelta) / (2*valora)

print(f'O valor de A é: {valora}, o valor de B é: {valorb}, o valor de C é: {valorc}, o valor de delta é: {delta} e as raízes são: {x1} e {x2}') 
