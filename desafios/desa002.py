a = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(a))        #tipo primitivo

print('É alfanumérico?', a.isalnum())                    #letras e números

print('É alfabético?', a.isalpha())                      #letras do alfabeto

print('É um número decimal?', a.isascii())               #números decimais

print('É um número decimal?', a.isdecimal())             #números decimais

print('É dígito?', a.isdigit())                          #dígitos

print('É um identificador?', a.isidentifier())           #identificador

print('Está em minúsculas?', a.islower())                #letras minúsculas

print('É um número?', a.isnumeric())                     #números

print('É imprimível?', a.isprintable())                  #caracteres imprimíveis

print('Só tem espaços?', a.isspace())                    #espaços em branco

print('Está capitalizada?', a.istitle())                 #primeira letra maiúscula

print('Está em maiúsculas?', a.isupper())                #letras maiúsculas