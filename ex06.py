num1 = int(input("Digite o primeiro numero:\n"))
num2 = int(input("Digite o segundo numero:\n"))
num3 = int(input("Digite o terceiro numero:\n"))

nums = [num1, num2, num3]

nums.sort(reverse=True)

print("Valores em ordem decrescente:")
for valor in nums:
    print(valor)