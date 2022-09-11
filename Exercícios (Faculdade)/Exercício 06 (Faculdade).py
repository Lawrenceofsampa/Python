'''Faça um algoritmo que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem
 e visualize o valor total a ser pago, considerando os 10% do garçom.'''
while True:
    print(' -ComaBem restaurante- ')
    Gasto = float(input('Entre com o seu gasto: '))
    Gorjeta = 10
    Conta = (Gorjeta * Gasto) / 100
    print(f'A sua conta deu um total de R$ {Conta + Gasto:3.2f}')

