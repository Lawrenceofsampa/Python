user1 = int(input('(1) Número: '))
user2 = int(input('(2) Número: '))
def maior(a , b):
    if a > b:
        return f'{a} é maior que {b}'
    else:
        return f'{b} é maior que {a}'
        
print(maior(user1, user2))