num1 = int(input("Digite o primeiro numero:\n"))
num2 = int(input("Digite o segundo numero:\n"))

dif1 = num1 - num2
dif2 = num2 - num1

if num1 > num2:
    print(f"A diferenca é de: {dif1}.")
else:
    print(f"A diferenca é de: {dif2}.")