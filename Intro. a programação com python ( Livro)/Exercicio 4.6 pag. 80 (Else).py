  #First attempt:

while True:
        
    distância = int(input('Entre com a distâcia: '))
    conta = distância

    if distância <= 200:
        conta = conta * 0.50
        print('Você precisa pagar, no total: ' , conta)

    else:
        conta = (conta * 0.45)
        print('Voce precisa pagar: ' , conta)


  #Correção:
        
'''distância = float(input("Digite a distância a percorrer: "))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância
print(f"Preço da passagem: R$ {passagem:7.2f}")'''

