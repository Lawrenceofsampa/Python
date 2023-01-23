while True:
    guardaExpressao = []
    contador = 0
    contador2 = 2
    expressao = input('Entre com a expressão em parenteses: ')
    guardaExpressao.append(expressao)
    if expressao == '()' :
        print('Ok')
        print(guardaExpressao)
    elif len(expressao) == contador2:
        print('OK')
    elif len(expressao) > contador2:
        contador = len(expressao)
        while contador2 < contador:
            contador -= contador2
        if contador == 2:
            print('OK')
            print(guardaExpressao)
        else:
            print('Erro')
            print(guardaExpressao)
    else:
        print('Erro')
    
        




