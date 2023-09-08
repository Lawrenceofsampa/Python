def MDC(a,b):
    if b == 0: #Se um dos números é 0 o outro é o divisor comum, ou seja, "a"
        return a
    else:
        return MDC(b, a % b) #Leia-se "b" é igual ao que sobra da divisão de "a" por "b"
while True:
    maiorNumero = int(input('Entre com o número (1): '))
    menorNumero = int(input('Entre com o número (2): '))
    if maiorNumero > menorNumero:
        print(MDC(maiorNumero, menorNumero))
    else:
        print(MDC(menorNumero , maiorNumero))

        '''
        As variáveis a e b não foram definidas em lugar algum.O correto seria comparar as variáveis maiorNumero e menorNumero. Por isso usar maior/menorNumero no lugar de a ou b
        '''


