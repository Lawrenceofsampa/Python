def retangulo(largura, altura,caractere = '*'): 
    linha = caractere * largura
    for i in range(altura):
        print (linha)
retangulo(3, 4)