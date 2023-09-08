while True:
    vS = input('Entre com a string para validar: ')
    def Valida(min, max):
        if len(vS) > max or len(vS) < min:
            return False
        else:
            return True
    if Valida(0, 5):
        print("String válida")
    else:
        print("String inválida")

    