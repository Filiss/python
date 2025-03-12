vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('Você execeu a velocidade permitida que é de 80km/h. Você foi MULTADO!')
    multa = (vel - 80) * 7
    print(f'Você deve pagar uma mulda de R${multa:.2f}!')
else:
    print('Você está dirigindo na velocidade permitida! Mantenha-se assim e dirija com segurança!')