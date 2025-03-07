import math

cateto1 = float(input('Digite o valor do cateto oposto:'))
cateto2 = float(input('Digite o valor do cateto adjacente:'))

hipotenusa = math.sqrt(cateto1*cateto1 + cateto2*cateto2)

print(f'O valor do cateto oposto é: {cateto1}, o valor do cateto adjacente é: {cateto2} e o valor da hipotenusa é: {hipotenusa :.2f}')