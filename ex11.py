nivel = int(input("Qual o nivel do professor:\n"))
horas = int(input("Quantas hora/aula o professor da por semana:\n"))

n1 = 12 * horas * 4.5
n2 = 17 * horas * 4.5
n3 = 25 * horas * 4.5

if nivel == 1:
    print(f"O salario do professor sera de R${n1:.2f}")
elif nivel == 2:
    print(f"O salario do professor sera de R${n2:.2f}")
elif nivel == 3:
    print(f"O salario do professor sera de R${n3:.2f}")
else:
    print("Nivel Invalido")