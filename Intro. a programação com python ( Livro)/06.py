a = 5
def mudaEImprime():
    global a
    a = 7 
    print(f'A dentro da função: {a}')
print(f'a antes de mudar: {a}')
mudaEImprime()
print(f'A depois de mudar: {a}')