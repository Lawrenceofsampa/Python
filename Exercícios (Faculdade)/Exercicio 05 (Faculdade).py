'''Faça um algoritmo que leia dois valores inteiros representando, respectivamente,
 um valor de hora e um de minutos e informe quantos minutos se passaram desde o início do dia. Exemplo:
valores lidos: 13 e 15 impressão: 795 minutos'''

while True:
    Horas = int(input('Entre com as horas: '))
    Minutos = int(input('Entre com os minutos: '))
    Hr = Horas * 60
    Mn = Minutos + Hr
    print(f'Passaram, num total, {Mn} minutos. ')