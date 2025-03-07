import math

catetoop = float(input('Digite o cateto oposto: '))
catetoad = float(input('Digite o cateto adjacente:'))

hipotenusa = (catetoop*catetoop + catetoad*catetoad)

sen = catetoop / hipotenusa
cos = catetoad / hipotenusa 
tg = catetoop / catetoad

print(f'O valor do cateto oposto é: {catetoop}, o valor do cateto adjacente é: {catetoad}, o valor da hipotenusa é: {hipotenusa :.2f}')
print(f'O valor do seno é: {sen :.2f}, o valor do cosseno é: {cos :.2f} e o valor da tangente é: {tg :.2f}')

#CALCULO DO SENO, COSSENO E TANGENTE A PARTIR DO CATETO OPOSTO, ADJACENTE E A HIPOTENUSA