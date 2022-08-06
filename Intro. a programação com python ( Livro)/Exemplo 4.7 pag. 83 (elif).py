while True:
    categoria = int(input('Entre com a categoria: '))
    if categoria == 1:
        preço = 10
    elif categoria == 2:
        preço = 18
    elif categoria == 3:
        preço = 23
    elif categoria == 4:
        preço = 26
    elif categoria == 5:
        preço = 31
    else:
        print('Categoria inválida, digite outro valor entre 1 e 5')
        preço = 0
    print (f'O preço do produto é: R${preço:6.2f}')

#Else + If = Elif
#Elif serve tanto para else quanto para if
#Uma forma de diminuir os if do programa que me será muito útil

