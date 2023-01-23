'Crie um algoritmo que leia o raio (r) e a altura(a) fornecidas pelo usuário e calcule o volume do cilindro.'
'Volume = ∏ * raio² * altura'

while True:
    Raio = int(input('Entre com o raio (r): '))
    Altura = float(input('Entre com a altura (a): '))
    r = Raio * Raio
    a = Altura
    Volume =  (3.14 * r) * a

    print(f'O volume é: {Volume:6.2f}')
