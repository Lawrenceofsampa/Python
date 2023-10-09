import sqlite3
from contextlib import closing
pedeParametro = input("Nome a selecionar: ")
with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute('select * from agenda where nome = ?  ', (pedeParametro,))
        contaResultado = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if contaResultado == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            contaResultado += 1
