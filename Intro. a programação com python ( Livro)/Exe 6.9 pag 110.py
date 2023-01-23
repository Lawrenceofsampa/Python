L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
p2 = int(input("Digite o segundo valor a procurar: "))
x = 0
while x < len(L): 
    if L[x] == p : #Se L e x forem iguais a p
        print(f"{p} achado na posição {x} da lista variável p1")
        break
    if L[x] == p2:
        print(f"{p2} achado na posição {x} da lista variável p1")
        break
    else:
        print('Deu merda')
    x += 1
