# Digita-se as variáveis para interação 
# Digita-se as variáveis para armazenar os maiores valores que irão ser identificados pelo programa


while True:
    primeiro = int(input('Primeiro numero: '))
    segundo = int(input('Segundo numero : '))
    terceiro = int(input('Terceiro numero: '))

    maior = primeiro
    menor = segundo

    if (segundo > maior):
        maior = segundo

        
    if (terceiro > maior):
        maior = terceiro

    if (terceiro <= menor):
        menor = terceiro

    if (primeiro <= menor):
        menor = primeiro

    print('Maior: ', maior)
    print('Menor: ' , menor)


    



    
