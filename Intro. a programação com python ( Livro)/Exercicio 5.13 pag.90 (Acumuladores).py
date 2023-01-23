while True:
    divida = float(input('Entre com o valor inicial da divida: '))
    taxa = int(input('Entre com o juro mensal: '))
    pagamento = float(input('Entre com o valor pago mensalmente: '))
    juroMensal = taxa / 100
    contaMes = 1
    juros_pago = 0
    if (divida * (taxa/100) > pagamento):
        print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
    else:
        while pagamento > divida:
                juros = divida * taxa / 100
                divida += juros - pagamento
                contaMes += 1
                juros_pago += juros
                print(f'Para pagar uma dívida de R${divida}, a {juros}% de juros')
                print(f'Vc vai precisar de: {contaMes - 1} meses e {juros_pago} juros por ano')
                print(f'O total seria, no último mês {divida}')
    