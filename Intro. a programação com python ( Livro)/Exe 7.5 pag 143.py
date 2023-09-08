sequencia = input("Digite a string: ")
segundaString = {}
terceiraString = {}

for letra in sequencia:
    segundaString[letra] = segundaString.get(letra, 0) + 1

for chave, valor in segundaString.items():

    print(f"{chave}: {valor}x")



    "Não entendi a solução, tão pouco o problema"