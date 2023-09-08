def MDC(a,b):
    if b == 0: #Se um dos números é 0 o outro é o divisor comum, ou seja, "a"
        return a
    else:
        return MDC(b, a % b) #Leia-se "b" é igual ao que sobra da divisão de "a" por "b"
def MMC(a,b):
    return abs(a * b) / MDC(a, b) #a função return abs(a * b) / MDC(a, b) não é recursiva. Ela simplesmente utiliza o resultado da função MDC(a, b) para calcular o MMC de a e b.
while True:
    maiorNumero = int(input('Entre com o número (1): '))
    menorNumero = int(input('Entre com o número (2): '))
    if maiorNumero > menorNumero:
        print(MMC(maiorNumero, menorNumero))
    else:
        print(MMC(menorNumero , maiorNumero))