#Exercicio 3.11 pag. 72 int input

while True:
    mercadoria = int(input('Digite o preço da mercadoria: '))
    desconto = int(input('Digite o  percentual de desconto: '))
    calculo = mercadoria * desconto // 100 - mercadoria

    print('O valor do desconto é: ' , calculo)
