armazena = []
largura = 76
max = 60

with open('nomes.txt') as nomes:
    for lista in nomes.readlines():
        nomes_separados = lista.split()
        armazena.append(' '.join(nomes_separados))
        print(''.join(armazena))