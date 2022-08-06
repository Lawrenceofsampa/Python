#Exercicio 3.14 pag. 72 int input

while True:
    km_percorridos = int(input('Entre com os km: '))
    dias = int(input('Entre com os dias: '))
    calculo = (dias * 60) + km_percorridos  * 0.15
    print ('O total a pagar é: ' , calculo)
