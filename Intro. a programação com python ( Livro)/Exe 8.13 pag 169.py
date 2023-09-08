def Valida(A,B,C):
    while True:
        options = input('Entre com a opção: ')
        for opcoes in options:
            if opcoes == Valida(A, B, C):
                return True
                guardaLetra += opcoes.lower()
            else:
                return False
                break
                


        

