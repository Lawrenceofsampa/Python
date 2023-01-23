while True:
    a = int(input("Entre com o primeiro número: "))
    b = int(input("Entre com o segundo número: "))
    a1 = a
    if a == 0 or b == 0:
        print('Inválido!')
        break
    else:
        contador = 0
        resto = a
        while a1 >= b:
            a1 -= b
        resto = a1
        print(f'O resto é: {resto}')


