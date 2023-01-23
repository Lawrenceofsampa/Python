while True:
    import math

    a = float(input("Digite o lado cercado a do terreno, em m: "))

    b = float(input("Digite o lado cercado b do terreno, em m: "))

    h = math.sqrt(a * a + b * b)  # ou:  math.sqrt( a**2 + b**2 )

    print("Terá que comprar ", h, " m (metros) de cerca.")
