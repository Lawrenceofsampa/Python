def soma(a , b):
    return a + b
def subtracao (a , b):
    return a - b
def imprime (a,b,foper):
    print(foper(a,b)) #Parâmetro
imprime(5,4,soma)
imprime(10,1,subtracao)