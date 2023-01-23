while True:
  valor = int(input('Entre com o valor a pagar: '))
  cedulas = 0
  atual = 100
  apagar = valor
  while True:
    #Se o valor pedido é menor do que a variável atual, simplesmente subtraia ela pelo valor pedido:
    
    if atual <= apagar:
        apagar -= atual 
        cedulas += 1
      #Se este não for o caso:
      
    else:
        print(f'{cedulas} cédula(s) de R$ {atual}') #Print fixo
        if apagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20: #Se o que sobra é 20
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01                            
        cedulas = 0 # Cada subtração é equivalente a contagem de uma cédula