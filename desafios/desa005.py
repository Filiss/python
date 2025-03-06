numero = float(input("Digite um número:"))
numerp = float(input("Digite outro número:"))

soma = numero + numerp
media = soma / 2

print(f"Suas duas notas são {numero} e {numerp}. A soma dos números é {soma :.1f} e a média é {media :.1f}")
# .format(numero, numerp, soma, media))