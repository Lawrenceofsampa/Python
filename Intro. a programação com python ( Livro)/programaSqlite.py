import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('''
                CREATE TABLE agenda(nome text,
                 telefone text)
                ''')
cursor.execute('''
                INSERT INTO agenda (nome, telefone) VALUES(?,?)
                ''', ('Nilo', '7788-1432'))
conexao.commit()
cursor.close()
conexao.close()