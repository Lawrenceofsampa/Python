estoque = {"tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100,1.50]}
solicitaProduto = input('Entre com o produto: ')
produto = solicitaProduto
while True:
    if solicitaProduto in estoque: #in Para saber se produto existe na tabela
        solocitaQuantidade = int(input('Entre com a quantidade (0 Para voltar): '))
        quantidade = solocitaQuantidade
        if solocitaQuantidade <= estoque[produto][0]:
            estoque[produto][0] -= quantidade
            preco = estoque[produto][1] * solocitaQuantidade
            print(f'Você deve pagar {preco}')
            print('Estoque: ' , estoque[produto][0])
        else:
            print('A quantidade ultrapassa a disponivel')
    else:
        print('Não encontrado!')
