def calcular_notas(valor):
    notas100 = 0
    notas50 = 0
    notas10 = 0
    notas5 = 0
    notas1 = 0

    if valor >= 100:
        notas100 = valor // 100
        valor = valor % 100

    if valor >= 50:
        notas50 = valor // 50
        valor = valor % 50

    if valor >= 10:
        notas10 = valor // 10
        valor = valor % 10

    if valor >= 5:
        notas5 = valor // 5
        valor = valor % 5

    notas1 = valor

    print("Notas de 100: ", notas100)
    print("Notas de 50: ", notas50)
    print("Notas de 10: ", notas10)
    print("Notas de 5: ", notas5)
    print("Notas de 1: ", notas1)


valor = int(input("Digite o valor em reais:\n"))
calcular_notas(valor)
