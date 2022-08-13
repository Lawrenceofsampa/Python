while True:
    Contador = 1
    Acumulador = 0
    Acumulador1 = 0
    while Contador <= 24:
        Depósito = float(input('Valor depositado: '))
        Juros = float(input('Entre com os juros atuais: '))
        print(f'{Contador} Você depositou um total de R$:{Acumulador:6.2f} numa taxa de juros acumulada de {Acumulador1} ')
        Contador = Contador + 1
        Acumulador = Depósito + Acumulador
        Acumulador1 = Juros + Acumulador1
    print(f'Você recebeu um total de R$: {(Acumulador * Acumulador1)/100} numa taxa de juros anual de {Acumulador1}')
