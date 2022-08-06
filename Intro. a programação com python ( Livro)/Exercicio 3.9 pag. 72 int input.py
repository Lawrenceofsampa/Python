#Exercicio 3.9 pag. 72:

while True:

    dias = int(input("Dias: "))
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
    print("Convertido em segundos é igual a:" , total_em_segundos)

