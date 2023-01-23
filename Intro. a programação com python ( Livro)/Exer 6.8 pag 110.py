while True:
    l = [15,7,27,39]
    p = int(input('Entre com o número para pesquisa-lo: '))
    contador = 0
    while contador < len(l):
        if l[contador] == p:
            print(f'{p} Achado na posição {contador}')
        elif l[contador] >= p and l[contador] <= l[contador]:
            print('Não econtrado')
        contador += 1