lista_de_palavras = []
armazenaPalavras = input("Entre com a lista de palavras (0 para sair): ").lower().strip()
while armazenaPalavras != '0':
    lista_de_palavras.append(armazenaPalavras)
    armazenaPalavras = input("Entre com a lista de palavras (0 para sair): ").lower().strip()
numero = int(input('Entre com um número: '))
letrasTentadas = []
acertos = []
erros = 0
indice = (numero * 776) % len(lista_de_palavras)
palavra = lista_de_palavras[indice]
while True:
    if numero > len(lista_de_palavras):
        print('Número informado maior do que o de palavras disponiveis')
        break
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra:").lower().strip()

    if tentativa in letrasTentadas:
        print("Você já tentou esta letra!")
        continue

    else:
        letrasTentadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""

    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "

    print(f"X{linha2}")

    linha3 = ""

    if erros == 5:

        linha3 += " /   "

    elif erros >= 6:

        linha3 += " / \ "

    print(f"X{linha3}")

    print("X\n===========")

    if erros == 6:

        print("Enforcado!")
        print(f'A palavra secreta era: {palavra}')
        break