primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posição = segunda.find(letra)
        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(f"Os caracteres {segunda} foram substituidos por "
              f"{terceira} em {primeira}, gerando: {resultado}")
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")



    '''    Pede ao usuário para digitar três strings, "primeira", "segunda" e "terceira".

    Verifica se o tamanho de "segunda" e "terceira" são iguais. Se não forem iguais, imprime uma mensagem de erro indicando que as duas strings precisam ter o mesmo tamanho.

    Se o tamanho das duas strings for igual, o código entra em um loop for que percorre cada letra na "primeira" string.

    Para cada letra, o código usa o método find() para encontrar a posição da letra na string "segunda".

    Se a posição não for -1, ou seja, se a letra estiver presente na string "segunda", o caractere correspondente na string "terceira" é adicionado à string "resultado".

    Se a posição for -1, ou seja, se a letra não estiver presente na string "segunda", a letra é adicionada à string "resultado" sem modificações.

    O loop for é repetido para cada letra na "primeira" string até que todas as letras tenham sido verificadas.

    Se a string "resultado" for vazia, imprime uma mensagem indicando que todos os caracteres foram removidos. Caso contrário, imprime uma mensagem mostrando o resultado final da substituição dos caracteres na string "primeira".
    '''