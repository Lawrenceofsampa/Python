import sqlite3
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('''
                SELECT * FROM precos
                ''')
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f'Produto: {resultado[0]}\n Preço: {resultado[1]}')
cursor.close()
conexao.close()