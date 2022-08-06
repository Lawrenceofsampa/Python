categoria = int(input('Entre com a categoria: '))
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else:
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print('Categoria inválida, digite outro valor entre 1 e 5')
                    preço = 0
print(f'O preço do produto é: R${preço:6.2f}')

'Reescrevi o código, só que desta vez, não usei o while True para que, exatamente como esta no livro, as numerações estejam corretas e eu posso comparar' \
'a execução de cada linha '
'A execução do código vai da numeração 1 a 19, respectivamente'
''