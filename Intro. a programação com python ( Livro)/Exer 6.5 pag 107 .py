ultimo = 10
fila = list(range(1, ultimo + 1 )) #Range para adicionar números conforme vc queira, neste caso, adicionando números de um a 10
x = 0
while True:
    print (f'\n Existem {len(fila)} clientes na fila.') #Números de elementos na fila
    print (f'\n Fila atual: {fila}')
    print('Digite F para acionar um cliente ao fim da fila, ou A para realizar o atendimento. S para Sair.')
    operacao = input('Operação (F, A ou S): ')
    while x < len(operacao):
        if operacao[x] == 'A': #Operação[x] para identificar quantos As foram

            if len(fila) > 0:
                atendido = fila.pop(0)
                print (f'Cliente {atendido} atendido')
            else:
                print('\n Fila vazia')
        elif operacao[x] == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == 'S':
            break
        else:
            print(f'Operação inválida: {operacao[x]} na posição {x}! Digite apenas F, A ou S!')
        x += 1
    if operacao[x] == 'S':
        break
    x = 0
