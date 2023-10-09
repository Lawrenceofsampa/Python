import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""UPDATE agenda
                        SET telefone = '12345-6789' """)
        print("Registros alterados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexao.commit()
            print('Alterações gravadas')
        else:
            conexao.rollback()
            print('Abortado!')