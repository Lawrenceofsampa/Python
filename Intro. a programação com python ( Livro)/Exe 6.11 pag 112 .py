L = []
while True:
    n = int(input('Entre com um número (0 Para sair): '))
    if n == 0:
        break
    L.append(n)
    #Este while não pode ser substituido pois tem a função de guardar os valores digitados na lista se fosse em for ele não repetiria n pois não possui parametro de True ou False
for x in L:
    print(x)
'''while x < len(L):
    print(L[x])
    x += 1'''