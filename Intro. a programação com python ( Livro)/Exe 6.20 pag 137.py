
L1 = [1, 2, 6, 8]
L2 = [3, 8, 9,45,789,45]

print(f"Lista 1: {L1}")
print(f"Lista 2 (Alterada): {L2}")

conjunto_1 = set(L1)
conjunto_2 = set(L2)

print(f'Valores novos: {conjunto_2 - conjunto_1}')
print(f'Valores que não mudaram: {conjunto_1 & conjunto_2}')
print(f'Elementos removidos: {conjunto_1 - conjunto_2}')


'''
# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)

# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A
print("Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)

# Repetido:
print("Primeira lista, sem os elementos repetidos na segunda:",
      conjunto_1 - conjunto_2)
'''