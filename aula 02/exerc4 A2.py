#exercicio 4
temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for i in temperaturas:
    if i < 37.5:
        print(f"{i}, Normal")
    elif i <= 38.5:
        print(f"{i}, Febre moderada")
    elif i > 38.5:
        print(f"{i}, Febre alta")
