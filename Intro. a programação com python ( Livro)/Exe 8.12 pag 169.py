while True:
    lista = int(input('Entre com o número: '))
    palavra = input('Entre com a palavra: ')
    guardaValor = []
    guardaValor.append(lista)
    
    def Valida(min, max):
        if len(palavra) > max or len(palavra) < min:
            return False
        else:
            if len(palavra) == lista:
                return True
            else:
                return False
    
    resultado = Valida(0, 5)
    print(resultado)
    
    if resultado == True:
        break
