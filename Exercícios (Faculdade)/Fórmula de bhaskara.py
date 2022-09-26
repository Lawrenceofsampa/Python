''' .Calcule as duas raízes de uma equação de 2º grau ax2 +bx + c, conhecendo os valores dos coeficientes da mesma (a,b,c).
 Suponha que as raízes são reais.
Lembrar que para calcular as duas raízes:
X 1,2 = -b ± √delta/2 a.
 Sendo que: delta  =  b2 – 4 a c'''

while True:
    print('Em busca de delta...')
    A = float(input('Entre com o valor de A: '))
    B = float(input("Entre com o valor de B: "))
    C = float(input('Entre com o valor de C: '))
    Delta = (B ** 2) - (4 * A * C)
    print('------------------------------------------------------------------')
    if A == 0:
        print('A deve possuir valor acima de 0!')
    elif Delta < 0:
        print('Sem raízes reais!')

    else:
        x1 = (-B + Delta ** (1/2)) / (2 * A)
        x2 = (-B - Delta ** (1/2)) / (2 * A)
        print(f'O valor de x1 é: {x1:0.0f}')
        print(f'O valor de x2 é: {x2:0.0f}')
        print('--------------------------------------------------------------------')






