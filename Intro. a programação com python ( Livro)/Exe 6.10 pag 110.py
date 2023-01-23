L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
p2 = int(input("Digite o valor a procurar:"))
x = 0
while x < len(L):
    if L[x] == p:
        break
    x += 1
if x < len(L):
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")

while x < len(L):
    if L[x] == p2:
        break
    x += 1
if x < len(L):
    print(f"{p2} achado na posição {x}")
else:
    print(f"{p2} não encontrado")