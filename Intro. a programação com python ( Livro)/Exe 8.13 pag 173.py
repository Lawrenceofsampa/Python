
def imprimeLista(L, fImpressao , fCondicao):
    for e in L:
        if fCondicao(e): #Se fCondicao, que é definido em imprimeLista como epar/eimpar for verdadeira, imprimeElemento é chamado. 
            fImpressao(e)
def imprimeElemento(e):
    print(f'Valor: {e}')
def epar(x):
    return x % 2 == 0
def eimpar(x):
    return not epar(x)
L = [1,7,9,2,11,0]
imprimeLista(L, imprimeElemento, epar) #Define os valores como as funções acima 
