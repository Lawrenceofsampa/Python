largura = 76
max = 60
with open('arquivoTexto.txt') as arquivoTexto:
  with open('paginado.txt', 'w') as paginado:
    for linha in arquivoTexto.readlines():
      if len(linha.rstrip()) > max:
        if linha and len(linha.rstrip()) <= largura:
          paginado.write(linha)






