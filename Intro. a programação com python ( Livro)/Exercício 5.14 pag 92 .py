guardaPreco = 0.00
while True:
    codigoProduto = int(input('Entre com o código do produto: '))
    preco = 0
    if codigoProduto == 0:
        break
    elif codigoProduto == 1:
        preco = 0.50
    elif codigoProduto == 2:
        preco = 1.00 
    elif codigoProduto == 3:
        preco = 4.00
    elif codigoProduto == 5:
        preco = 7.00
    elif codigoProduto == 9:
        preco = 8.00
    else:
        print("Inválido!")

    if codigoProduto != 0:
        quantidadeComprada = int(input('Entre com a quantidade comprada: '))
        guardaPreco += (preco * quantidadeComprada)
print(f'Vc precisa pagar R$ {guardaPreco:8.2f}')



