L = [1,2,3,4,5]
fim = len(L) #5
while fim > 1:
    trocou = False
    x = 0 #Contador/Índice
    while x < (fim - 1):
        if L[x + 1] > L[x]: #É como L[x] fosse L[0], mas x é um contador. O outro é como se fosse L[1], imagine que estivesse comparando o primeiro índice com o outro, x serve apenas como meio para que isso seja possível, já que este começa com 0.
            trocou = True
            temporaria = L[x + 1] #7
            L[x + 1] = L[x] #Primeiro elemento vai passar a ser o segundo
            L[x] = temporaria
        x += 1
        print('x é: ' , x)
    if not trocou: #Se nenhum elemento foi trocado, Break
        break
    fim -= 1 #Somente aqui fim será realmente alterado
for e in L:
    print('O valor de e: ' , e)
