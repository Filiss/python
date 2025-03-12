a = int(input('Primeiro número:'))
b = int(input('Segundo número:'))
c = int(input('Terceiro número:'))

if a > b and a > c:
    print(f'O maior número é {a}')
if b > a and b > c:
    print(f'O maior número é {b}')
if c > a and c > b:
    print(f'O maior número é {c}')

if a < b and a < c:
    print(f'O menor númeor é {a}')
if b < a and b < c:
    print(f'O menor número é {b}')
if c < a and c < b:
    print(f'O menor número é {c}')

