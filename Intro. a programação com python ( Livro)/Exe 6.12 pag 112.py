'''
L = list(range(100,1100,50))
print(L)
'''

'''
for v in range(3,33,3): # range(começa de tal,até tal,de tal em tal)
    print(v, end= ' ') #Não pule linhas com end = ' '
print() 
'''
'''L = [5,9,13]
for x, e in enumerate(L):
    print(f'[{x}] {e}')'''

L = [1,7,2,4]
maximo = L[0]
for e in L: #Imprime e até chegar no segundo índice e, se constatado ser maior que maximo, imprime maximo que agora equivale a e (7)
    if e > maximo:
        e = maximo
        print(e)
        break