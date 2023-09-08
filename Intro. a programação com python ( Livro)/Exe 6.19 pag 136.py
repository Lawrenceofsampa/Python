while True:
    l1 = set([56,78,99,22,23,45])
    l2 = set([45,88,4,7,78,41])
    l3 = []
    l4 = []
    contador = 0
    while len(l3) < 6 and len(l4) < 6:
        interacao = int(input('Entre com o número (0 Para sair): '))
        contador += 1
        if interacao == 0:
            break
        else:
            if interacao in l1 and l2:
                l3.append(interacao)
                
            elif interacao not in l1 and l2:
                l4.append(interacao)
            if interacao in l3:
                interacao * 2
                l4.append(interacao)
    print('Valores comuns às duas listas (l3): ' , l3)
    print(f'Nova lista: {l4}')
    break
        
        
   
