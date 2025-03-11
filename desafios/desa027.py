frase = input('Digite uma frase:')

print(f'A letra "a" aparece {frase.lower().count("a")} vezes')
print(f'A primeira letra "a" apareceu na posição {frase.lower().find("a") + 1}')
print(f'A última letra "a" apareceu na posição {frase.lower().rfind("a") + 1}')