L = []
L1 = []
with open('pares.txt') as pares:
    for n in pares.readlines():
        L.append(int(n))
        L1 = list(set(L))
        L1.reverse()
        with open('reversedPar.txt', 'w') as reversedPar:
            for x in L1:
                reversedPar.write(str(f'{x}\n'))
        reversedPar.close()