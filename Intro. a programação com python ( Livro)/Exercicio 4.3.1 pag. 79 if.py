#
while True:
         
    Var1 = int(input('Entre com a primeira variável: '))
    Var2 = int(input('Entre com a segunda variável : '))
    Var3 = int(input('Entre com a treceira variável: '))
    num1 = Var1
    num2 = Var2
    num3 = Var3

    if Var1 > Var2 or Var2 > Var1:
        num2 = 0
        num3 = 0
    print(f'O número {Var1} da variação 1 é o maior de todos')


    if Var2 > Var1 or Var2 > Var3:
        num1 = 0
        num3 = 0
    print(f'O número {Var2} da variação 2 é o maior de todos')

    if Var3 > Var2 or Var3 > Var1:
        num2 = 0
        num1 = 0
        print(f'O número {Var3} da variação 3 é o maior de todos')



    



    
