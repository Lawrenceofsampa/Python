while True:
    velocidade = int(input('Qual velocidade do veiculo?: '))
    multa = (velocidade - 80) * 5

    if velocidade > 79:
        print(f'Você foi multado em {multa} R$ por ultrapassar o limite em Km/h!')

#Inicialmente, eu tinha posto o calculo como soma, mas o correto é por multiplicação

        
