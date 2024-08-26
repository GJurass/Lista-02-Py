def é_tri (x,y,z):
    return (x < y + z) and (y < x + z) and (z < x + y)

def tipo_tri (x,y,z):
    if x == y == z:
        return "Equilatero"
    elif x == y or y == z or z == x:
        return "Isosceles"
    else:
        return "Escaleno"

x = float(input("Digite o primeiro valor:\n"))
y = float(input("Digite o segundo valor:\n"))
z = float(input("Digite o terceiro valor:\n"))

if é_tri(x,y,z):
    tipo = tipo_tri(x,y,z)
    print(f"Os valores formar um triangulo {tipo}.")
else:
    print("Os valores não formam um triangulo.")
