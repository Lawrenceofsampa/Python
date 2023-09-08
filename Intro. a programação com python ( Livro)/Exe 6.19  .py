'''
d = {}
palavra = 'banana'
for letra in palavra:
    if letra in d:
        d[letra] = d[letra] + 1
        print(letra)
        print(d)
    else:
        d[letra] = 1
        print(letra)
        print(d)
print(d)
print(letra)
'''
d = {}
palavra = 'banana'
for letra in palavra:
    d[letra] = d.get(letra , 0) + 1
    print(d)
    print(letra)
print(d)