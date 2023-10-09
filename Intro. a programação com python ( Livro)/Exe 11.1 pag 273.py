import sqlite3
conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute('''
                CREATE TABLE precos(nomeProduto text,
                 precoProduto text)
                ''')
cursor.execute('''
                INSERT INTO precos (nomeProduto, precoProduto) VALUES(?,?)
                ''', ('Refrigerante', '15.99'))
conexao.commit()
cursor.close()
conexao.close()