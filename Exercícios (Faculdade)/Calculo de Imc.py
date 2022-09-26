'''cálculo do IMC: peso/(altura*altura)
'''
while True:
    Peso = float(input('Entre com seu peso: '))
    Altura = float(input('Entre com a sua altura: '))
    Calculo = Peso / Altura ** 2
    if Calculo < 16:
        print(f'Seu IMC é de: {Calculo:6.1f} kg/m2.')
        print('Muito abaixo do peso!')
    elif Calculo < 17 :
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Abaixo do peso! ')
    elif Calculo < 25.99 :
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Peso normal')
    elif Calculo < 29.99:
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Acima do peso! ')
    elif Calculo < 34.99:
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Obesidade I')
    elif Calculo < 39.99:
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Obesidade II (severa)')
    elif Calculo > 40:
        print(f'Seu IMC é de:{Calculo:6.1f} kg/m2.')
        print('Obesidade III (mórbida)')