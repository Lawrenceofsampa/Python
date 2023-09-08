primeiraString = 'AABBEFAATT' 
segundaString = 'BE'

if segundaString in primeiraString:
    p = 0
    print('A string {segunda} esta presente na primeira string \n')
    while (p >= -1):
        p = primeiraString.find(segundaString, p)
        if p >= 0:
            print(f'Sua posição é: {p}')
            p += 1
else:
    print(f"A string {segundaString} não se encontra presente na primeira string.")



