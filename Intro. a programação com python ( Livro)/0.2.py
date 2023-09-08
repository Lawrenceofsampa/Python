'''
def soma (a,b):  
    return a + b 
print(soma(7, 9))
'''

'''
def parOuImpar(x):
    return x%2 == 0
print(parOuImpar(2))
print(parOuImpar(3))
print(parOuImpar(10))
'''
'''def parOuImpar(x):
    return x%2 == 0
def retornaStirng(x):
    if parOuImpar(x): #Se parOuImpar == True retorne string ''
        return 'Par'
    else:
        return 'Ímpar'
print(retornaStirng(2))
print(retornaStirng(3))
'''
'''def barra(x = 10, c='*'):
    print(c * x)
L = [[5, "-"],[10, '*'] , [5], [6 ,'.'] ]
for e in L:
    barra(*e)'''

'''def soma(*args):
    s = 0
    for x in args:
        s += x
    print (s)
soma(1, 2)
soma(2)
soma(5, 6, 7, 8)
soma(9, 10, 20, 30, 40)'''

'''def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)
imprime_maior("Maior:", 5, 4, 3, 1)
imprime_maior("Max:", *[1, 7, 9])'''

'''a = lambda x: x * 2
print(a(3))'''
'''aumento = lambda a, b: ((a * b) / 100)
print(aumento(100,5))'''

'''L = [2, 'Alo' , ['!'] , {"a": 1}]
for e in L:
    print(type(e))'''

ESPAÇOS_POR_NÍVEL = 4


def imprime_elementos(l, nivel=0):
    espacos = ' ' * ESPAÇOS_POR_NÍVEL * nivel
    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprime_elementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)


L = [1, [2, 3, 4, [5, 6, 7]]]

imprime_elementos(L)