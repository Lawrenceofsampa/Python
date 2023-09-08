primeiraString = input('Entre com a string (1): ') 
segundaString = input('Entre com a string (2): ')
terceiraString = ''
for letra in primeiraString:
    if letra not in segundaString:
        terceiraString += letra


