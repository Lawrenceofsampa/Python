contaPar = 0
contaImpar = 0
chegada = 0
with open('pareseimpares.txt' , 'w') as pareseimpares:
    with open('pares.txt') as pares, open('impares.txt') as impares:
        for n in pares.readlines():
            contaPar += 1
            for l in impares.readlines():
                contaImpar += 1
    ale = [contaImpar + contaImpar]
    while ale[0] > chegada:
        chegada += 1
        pareseimpares.write(str(f'{chegada}\n'))
pareseimpares.close()






