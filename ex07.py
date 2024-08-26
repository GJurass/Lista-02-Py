alt = float(input("Digite sua altura em metros:\n"))
sex = str(input("Digite seu sexo: (M ou F)\n")).upper()

if sex == "M":
    peso = (72.7 * alt) - 58
    print(f"Seu peso ideal é de {peso:.2f} kg")
elif sex == "F":
    pesof = (62.1 * alt) - 44.7
    print(f"Seu peso ideal é de {pesof:.2f} kg")
else:
    print("Sexo invalido")