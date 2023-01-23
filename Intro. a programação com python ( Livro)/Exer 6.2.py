ns = [0,0,0,0,0]
contaNumero = 0
while contaNumero < 5:
    ns[contaNumero] = int(input(f'Número {contaNumero + 1}: '))
    contaNumero += 1

while True:
    escolhido = int(input(f'Qual número deseja imprimir? (0 Para sair): '))
    if escolhido == 0:
        break
    print(f'Você escolheu o número: {ns [escolhido]}')

