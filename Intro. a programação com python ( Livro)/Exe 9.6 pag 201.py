largura = 40
parametro = ''
aleatorio = 0
with open('noventaESeis.txt') as noventaESeis:
    for linha in noventaESeis.readlines():
        if linha[0] == '=':
            print(largura * linha[0])
        elif linha[0] == '.':
            parametro += linha[0]
            while largura > aleatorio:
                parametro += parametro
                print(parametro)
                comando = int(input('Pressione qualquer número para continuar e ENTER para parar: '))
                if comando >= 0:
                    continue
                elif comando == '':
                    print('Finished')
                    break
        else:
            print(linha)
