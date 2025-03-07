import math

angulo = float(input('Digite o valor do ângulo:'))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print(f'O valor do seno é: {sen :.2f} \n O valor do cosseno é: {cos :.2f} \n O valor da tangente é: {tg :.2f}')