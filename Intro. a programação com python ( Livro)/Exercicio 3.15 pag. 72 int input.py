#Exercicio 3.15 pag. 72 int input
'------------------------------------------------------------------------'
#Dividindo a conta em dois fica mais fácil
#calcu1 para minutos perdidos em minutos e
#calcu2 para dias perdidos em minutos
#Transforme a idade do user em dias vividos e subtraia pela expectativa de vida
#Após isso, subtraia pelos dias que o cigarro custou a ele
#E, feito isso, converta em anos

while True:
    print ('--------------------------------------------------------------')
    Cigarros = int(input('-Entre com o número de cigarros que vc fuma ao dia: '))
    print ('--------------------------------------------------------------')
    Anos = int(input('-Entre com os anos que vc tem fumado: '))
    print ('--------------------------------------------------------------')
    Idade = int(input('-Entre com a sua idade: '))
    calculo1 = Anos * 365 * Cigarros * 10
    calculo2 = calculo1 // (24 * 60)
    calculo3 = (Anos * 365) - 27959 - calculo2
    calculo4 = calculo3 // 365
    #----------------------------------------------------------------------------------------print
    print ('--------------------------------------------------------------')
    print (f'-Você perdeu um total de {calculo1} minutos da sua vida!')
    print (f'Isso da um total de {calculo2} dias')
    print (f'Você ainda tem, considerando a expectativa de vida do brasil, {calculo3} dias para viver')
    print (f'Ainda lhe restão {calculo4} anos de vida')
