while True:
    clima = [-10,-8,0,1,2,5,-2,-4]
    maxima = clima[5]
    minima = clima[0]
    usuario = int(input('Entre com o que deseja saber \n (1 Para temperatura maxima 2 Para temp. minima e 3 para a media de temp.) : '))
    if usuario == 1:
        for e in clima:
            if e > maxima:
                maxima = e
            print(maxima)
            break
    elif usuario == 2:
        for e in clima:
            if e == minima:
                minima = e
                print(minima)
                break
    elif usuario == 3:
        for e in clima:
            if e == clima[6]:
                print(e)



                #Resposta: Não gostei muito da solução do autor


'''
T = [-10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0]  # A escolha do primeiro elemento é arbitrária, poderia ser qualquer elemento válido
máxima = T[0]
soma = 0
for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e
    soma = soma + e
print(f"Temperatura máxima: {máxima} °C")
print(f"Temperatura mínima: {mínima} °C")
print(f"Temperatura média: {soma / len(T)} °C")
'''