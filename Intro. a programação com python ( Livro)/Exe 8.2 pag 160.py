user1 = int(input('(1) Número: '))
user2 = int(input('(2) Número: '))
def eMultiplo(a , b):
    if a % b == 0 or a == 0 :
        return f'O número {a} é múltiplo de {b}' if a % b == 0 else f'O número {b} é múltiplo de {a}'
        return True
    else:
        return f'Os números {a} e {b} não são múltiplos entre si'
        return False

print(eMultiplo(user1, user2))