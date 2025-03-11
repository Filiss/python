#SOLETRA CADA LETRA DA PALAVRA SEPARADA POR ESPAÇO
def soletrar_palavra(palavra):
   print(" ".join(letra for letra in palavra))

palavra = input('Digite uma palavra: ')
soletrar_palavra(palavra)


#SOLETRA CADA LETRA DA PALAVRA EM UMA LINHA
def soletrar_palavra(palavra):
    for letra in palavra:
        print(letra)

palavra = input('Digite uma palavra: ')
soletrar_palavra(palavra)
