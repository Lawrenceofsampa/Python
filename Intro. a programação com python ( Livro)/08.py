while True:
    v = int(input('ENtre com um valor de 0 a 5: '))
    def MM(max,min):
        if v < min or v > max:
            print('Inválido!')
        else:
            print(v)
    MM(5, 0)
