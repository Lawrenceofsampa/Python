while True:
    tabuadaEscolhida = 1
    guardaValor = 1
    parametro = 10
    menu = int(input('Insira o número para escolher \n 1 - Para somar números \n 2 - Para subtração \n 3 - Para divisão e \n 4 - Para multiplicação \n 0 - para sair): '))
    while True:
        if menu == 0:
            break
        else:
            if menu == 1:
                while tabuadaEscolhida <= parametro:
                    guardaValor += 1
                    print(f'{tabuadaEscolhida} + {guardaValor} = {tabuadaEscolhida + guardaValor}')
                    if guardaValor == 11:
                        guardaValor = 1 # Se o valor chegar a 11 o guardaValor volta a ser um novamente e adiciona mais 1 na var. tabuadaEscolhida que esta logo acima
                        tabuadaEscolhida += 1
                break #Break para voltar ao while True inicial
            
            elif menu == 2:
                while tabuadaEscolhida <= parametro:
                    guardaValor += 1
                    print(f'{tabuadaEscolhida} - {guardaValor} = {tabuadaEscolhida - guardaValor}')
                    if guardaValor == 11:
                        guardaValor = 1
                        tabuadaEscolhida += 1
                break
            elif menu == 3:
                while tabuadaEscolhida <= parametro:
                    guardaValor += 1
                    if tabuadaEscolhida % guardaValor == 0:
                        print(f'{tabuadaEscolhida} / {guardaValor} = {tabuadaEscolhida / guardaValor}')
                    if guardaValor == 11:
                        guardaValor = 1
                        tabuadaEscolhida += 1
                break
            elif menu == 4:
                while tabuadaEscolhida <= parametro:
                    guardaValor += 1
                    print(f'{tabuadaEscolhida} x {guardaValor} = {tabuadaEscolhida * guardaValor}')
                    if guardaValor == 11:
                        guardaValor = 1
                        tabuadaEscolhida += 1
                break

            else:
                print('Comando inválido!')
            break #Break para voltar ao while True inicial


