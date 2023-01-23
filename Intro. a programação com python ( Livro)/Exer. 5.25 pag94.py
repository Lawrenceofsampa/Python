n = int(input("Entre com o número para calcular a raíz: "))
b = 2
p = (b + (n/b))/2 #Chute
quadrado = p * p
while quadrado - n > 0.0001:
    b = p #Atualiza b ao valor do p passado para calculá-lo logo abaixo 
    p = (b + (n/b))/2 #Atualiza valor de p
    quadrado = p * p #Calcula o novo valor de p ao quadrado
    print(f'{p}')




    
