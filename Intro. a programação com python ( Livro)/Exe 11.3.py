import sqlite3
from contextlib import closing
pedeParametro1 = input("Preço do produto 1: ")
pedeParametro2 = input('Preço do produto 2: ')
with sqlite3.connect("precos.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute('select * from precos where precoProduto >= ?   AND  select * from precos where precoProduto <= ?', (pedeParametro1,pedeParametro2))
        contaResultado = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if contaResultado == 0:
                    print("Nada encontrado.")
                break
            print(f"Nome: {resultado[0]}\nPreço: {resultado[1]}")
            contaResultado += 1