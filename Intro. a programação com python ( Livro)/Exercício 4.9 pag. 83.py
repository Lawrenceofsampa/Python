while True:
    casa = int(input('Entre com o valor da casa: '))
    salario = int(input('Entre com seu salário: '))
    anos = int(input('Entre com os anos: '))

    if casa > 0: 
        anos = (anos * 12) // casa
        salario = (salario * 30) / 100
    print(f'Vc deve pagar um total de R${salario:6.2f} em {anos} parcelas ')



    #Resposta:
    '''valor = float(input("Digite o valor da casa: "))
    salário = float(input("Digite o salário: "))
    anos = int(input("Quantos anos para pagar: "))
    meses = anos * 12
    prestacao = valor / meses
    if prestacao > salário * 0.3:
        print("Infelizmente você não pode obter o empréstimo")
    else:
        print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")'''
