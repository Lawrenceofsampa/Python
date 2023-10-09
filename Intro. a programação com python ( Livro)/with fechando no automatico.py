import sqlite3
from contextlib import closing
with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'Nome: {resultado[0]}\n Telefone: {resultado[1]}')