armazena = {}
with open('nomes.txt') as nomes:
    for lista in nomes.readlines():
        if lista not in armazena:
            armazena[lista] = len(lista[0])
            print(armazena)
