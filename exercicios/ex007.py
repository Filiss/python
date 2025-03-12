n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2) / 2

print(f'Sua média foi {m:.1f}')
if m >= 8.0:
    print('Sua média foi boa! PARABÉNS!')
elif m <= 7.0 and m >= 5.0:
    print('Sua média foi razoável!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')