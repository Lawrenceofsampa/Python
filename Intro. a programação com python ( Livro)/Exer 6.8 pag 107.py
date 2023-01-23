ultimo = 10
ultimo2 = 10
fila = list(range(1, ultimo + 1 )) #Range para adicionar números conforme vc queira, neste caso, adicionando números de um a 10
fila2 = list(range(1,ultimo2 + 1))
x = 0
while True:
    print (f'\n Existem {len(fila)} clientes na primeira fila. E {len(fila2)} clientes na segunda fila') #Números de elementos na fila
    primeira = input(f'\nQual fila você deseja acessar?(A Para primeira fila ou B para segunda fila) : ')
    if primeira == 'A' or primeira == 'a':
        print('\nDigite F para acionar um cliente ao fim da fila, ou A para realizar o atendimento. S para Sair.')
    elif primeira == 'B' or primeira == 'b':
        print('Digite G para acionar um cliente ao fim da fila, ou O para realizar o atendimento. S para Sair.')
    else:
        print('Comado inválido!')
    operacao = input('\nInsira o comando desejado: ')
    while x < len(operacao):
        if operacao[x] == 'A': #Operação[x] para identificar quantos As foram

            if len(fila) > 0:
                atendido = fila.pop(0) #Remove o item da lista, porém, mostra o item removido, diferente de del
                print (f'Cliente {atendido} atendido')
            else:
                print('\n Fila vazia')

        if operacao[x] == 'G':
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)

                print (f'Cliente {atendido2} atendido')
            else:
                print('\n Fila vazia')

        elif operacao[x] == 'O':
            ultimo2 += 1
            fila2.append(ultimo2)

        elif operacao[x] == 'F':
            ultimo += 1
            fila.append(ultimo)

        elif operacao[x] == 'S' :
            break
        
        else:
            print(f'Operação inválida: {operacao[x]} na posição {x}! Digite apenas F, A, G, O, ou S!')
        x += 1