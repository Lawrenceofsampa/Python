#Exercicio 3.10 pag. 72 int input
#while True para repetir o programa enquanto der True

while True:
    salario = int(input('Entre com o valor do salário: '))
    aumento = float(input('Entre com o valor do aumeto: '))
    calculo = salario * aumento /100
    print('O aumento foi de: ' , calculo)
