Salario = float(input('Entre com o seu salário: '))
conta1 = (Salario * 10) / 100
conta2 = (Salario * 15) / 100

if Salario > 1250.00:
    print(f'O seu aumento foi de {conta1:6.2f} R$')

if Salario <= 1250.00:
    print(f'O seu aumento foi de {conta2:6.2f} R$')
    
    
