l = []
while True:
    n = int(input('Entre com o número (0 Para sair): '))
    if n == 0:
        break
    l.append(n) #Adiciona os valores de n a l como lista
dizNumero = 0
while x < len(l):
    print(f'O número digitado foi: {l[dizNumero]}') #dizNumero para apontar qual ordem númerica começa a lista
    dizNumero += 1
