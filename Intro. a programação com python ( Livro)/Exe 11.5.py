import sqlite3
from contextlib import closing
produto = input('Entre com o produto: ')
preco = input('Entre com preço: ')
with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('UPDATE precos SET precoProduto = ? WHERE precoProduto = ? ' , (preco,produto,))
conexao.commit()