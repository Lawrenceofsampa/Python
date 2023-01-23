nota = [0,0,0,0,0,0,0,0,0] #[índices]
armazenaNota = 0
contaNota = 0
while contaNota < 8:
    
    nota[contaNota] = float(input(f'Nota {contaNota}: ')) #Entre com o valor inicial da lista
    armazenaNota += nota[contaNota] #Armazena o valor de notas somando todas elas e guardando o valor
    contaNota += 1
contaNota = 0 #Esta linha do código se encontra fora do loop, isto é, ela vai zerar o conta nota fazendo com que entre no próximo loop

while contaNota < 8:

    print(f'Nota {contaNota}: {nota[contaNota]: 6.2f}')
    contaNota+=1

print(f'Media {armazenaNota / contaNota:5.2f}')