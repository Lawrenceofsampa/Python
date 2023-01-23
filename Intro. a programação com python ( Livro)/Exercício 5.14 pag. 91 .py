contaNumero = 0
media = 0
while True:
    inteiro = int(input('Entre com o número: '))
    print(f'Vc digitou {inteiro}')
    contaNumero += 1
    media += inteiro
    if inteiro == 0:
        print(f'Foram digitados {contaNumero - 1} números')
        print(f'A média entre estes números é: { media / contaNumero + 2: 2.1f}')
        break


