'''

v = [7,8,32,5,6,46,48,12]
p = []
i = []

for e in v:
    print(e)

    if e % 2 == 0: #Par se a divisão por dois der zero

        p.append(e)
    else:

        i.append(e)

print(f'Pares: {p}')

print(f'Ímpares:  {i}')
'''


#

'''

lugares_vagos = [10,2,1,3,0]

while True:

    sala = int(input('Sala (0 Para sair): '))

    if sala == 0:

        break

    elif sala > len(lugares_vagos) or sala < 1:

        print('Sala indisponivel ou lugar inváido!')

    elif lugares_vagos[sala - 1] == 0:

        print('Sala lotada!')
    else:

        lugares = int(input(f'lugares vagos: ({lugares_vagos[sala - 1]})\n Entre com a qnt. de lugares: '))

        if lugares > lugares_vagos[sala - 1]:

            print('Número de lugares indisponível!')

        elif lugares < 0:

            print('Número inválido!')
        else:

            lugares_vagos[sala -1] -= lugares

            print(f'{lugares} lugares vendidos')

    print('Utilização das salas')

    for x, l in enumerate(lugares_vagos):

        print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')
'''


#

'''

L = ['maca' , 'pera' , 'kiwi']

for s in L:
    print(s)
    for letra in s:
        print(letra)
'''
'''

produto1 = ["maçã", 10, 0.30]

produto2 = ["pera",  5, 0.75]

produto3 = ["kiwi",  4, 0.98]

compras = [produto1, produto2, produto3]

for e in compras:

    print(f"Produto: {e[0]}")

    print(f"Quantidade: {e[1]}")

    print(f"Preço: {e[2]:5.2f}")
    '''
'''

compras = []

while True:

    produto = input("Produto: ")

    if produto == "fim":

        break

    quantidade = int(input("Quantidade: "))

    preço = float(input("Preço: "))

    compras.append([produto, quantidade, preço])

soma = 0.0

for e in compras:

    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")

    soma += e[1] * e[2]

print(f"Total: {soma:7.2f}")
'''


L = [7,4,3,12,8]
fim = len(L) #5
while fim > 1:
    trocou = False
    x = 0 #Contador/Índice
    while x < (fim - 1):
        if L[x] > L[x + 1]: #É como L[x] fosse L[0], mas x é um contador. O outro é como se fosse L[1], imagine que estivesse comparando o primeiro índice com o outro, x serve apenas como meio para que isso seja possível, já que este começa com 0.
            trocou = True
            temporaria = L[x] #7
            L[x] = L[x + 1] #Primeiro elemento vai passar a ser o segundo
            L[x + 1] = temporaria
        x += 1
        print(f'Valor de x: {x} \ Valor de Fim: {fim} \ Valor de L: {L} \  Valor temporária: {temporaria}')
    if not trocou: #Se nenhum elemento foi trocado, Break
        break
    fim -= 1 #Somente aqui fim será realmente alterado
for e in L:
    print('O valor de e: ' , e)



