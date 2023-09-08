def somaLista(lista):
    acumulaLista = 0
    for x in lista:
        acumulaLista += x
    return acumulaLista
lista = [1,7,2,9,15]
print(somaLista(lista))
print(somaLista([7,9,12,3,100,20,4]))