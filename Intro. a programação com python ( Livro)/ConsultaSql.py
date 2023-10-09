import sqlite3
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('''
                SELECT * FROM agenda
                ''')
resultado = cursor.fetchall()
for registro in resultado:
    print(f'Nome: {resultado[0]}\n Telefone: {resultado[1]}')
cursor.close()
conexao.close()