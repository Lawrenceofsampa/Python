arquiva = []
with open ('nomes.txt', 'w') as nomes:
    for lista in nomes.readlines():
        singular = set(arquiva)
        if lista[1] == lista[2]:

