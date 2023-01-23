l1 = []
l2 = []
l3 = []
x1 = 0
x2 = 9
contador = 0
while True:
    guardaLista1 = int(input(f'Entre com um número para primeira lista (0 Para sair): '))
    if guardaLista1 == 0:
        break
    l1.append(guardaLista1)
    x1 += 2
    l3.append(x1)
print(f'Primeira lista: {l1}')
while True:
    guardaLista2 = int(input('Entre com um número para segunda lista (0 Para sair): '))
    if guardaLista2 == 0:
        break
    x2 *= 2
    l3.append(x2)
    l2.append(guardaLista2)
print(f'Segunda lista: {l2}')
print(f'Terceira lista: {l3}')

    