
while True:
    salario = float(input('Digite o salário: '))
    base = salario
    imposto = 0
    if base > 3000:
        imposto = imposto + ((base - 3000) * 0.35)
        base =  3000
    if base > 1000:
        imposto = imposto + ((base - 1000) * 0.20)
    print(f'Sálario: R${salario:6.2f} imposto a pagar: R${imposto:6.2f}')


'''No caso, a isenção de imposto é aplicada nos valores iniciais e, somente
o restante tem impostos'''

'''Acima de 3000 são 35%, e acima de 1000, 20%.'''

'''6.2f Quer dizer o fatiamento de inicio e final como, por exemplo, o resultado
digitando 1700 é um imposto de 140.0 ele vai criar seis zeros para fatia-los
e colocar o ponto no caso criando-se seis zeros e fatiando estes para exibir
somente do segundo para trás: 140.00'''

'''Repetir a variável para que assim não a perca pois digitando uma nova variável
se perde ela e assim não se pode mais utiliza-la'''

'''No segundo if a variável base é atualizada mudando de equivalente a salário
para equivalente a 3000. Com isso é possivel utilizar a base com o valor atualizado
na conta'''

'''Atualiza-se o valor a=da variável base para 3000 no primeiro if'''
