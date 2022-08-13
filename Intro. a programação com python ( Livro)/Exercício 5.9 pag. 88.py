while True:
    print('------------------------Divisão de dois números através de contadores-----------------------')
    Primeiro = int(input('Entre com o primeiro número: '))
    Segundo = int(input('Entre com segundo número: '))
    Resultado = 0  # Contador
    x = Primeiro
    while x > Segundo:
        x = x - Segundo  # O que sobra daqui é resto
        Resultado = Resultado + 1
    Resto = x
    print('O resultado da divisão entre estes dois números é: ', Resultado)
    print('O resto da divisão é: ', Resto)






