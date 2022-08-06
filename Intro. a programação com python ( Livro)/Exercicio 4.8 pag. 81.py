while True:
    a = int(input('Entre com o primeiro número: '))
    b = int(input('Entre com o segundo número: '))
    c = int(input('''Entre com a operação que você deseja realizar com os números.
    1 Para Soma,
    2 Para Divisão,
    3 Para Subtração e
    4 Para multiplicação.
     Entre com a opção desejada: '''))

    if c == 1:
        print('Você escolheu somar!')
        print('O resultado da sua opção: ', a + b)

    elif c == 2:
        print('Você escolheu dividir!')
        print('O resultado da sua opção: ', a / b)

    elif c == 3:
        print('Você escolheu subtrair!')
        print('O resultado da sua opção: ', a - b)

    elif c == 4:
        print('Você escolheu multiplicar!')
        print('O resultado da sua opção: ', a * b)

    else:
        print('Opção inválida!')




