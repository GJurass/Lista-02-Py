sini = float(input("Digite o valor atual do salario:\n"))
cargo = str(input("Digite o cargo atual:\n")).lower()

c101 = sini * 1.1
c102 = sini * 1.2
c103 = sini * 1.3
c104 = sini * 1.4

dif1 = c101 - sini
dif2 = c102 - sini
dif3 = c103 - sini
dif4 = c104 - sini

if cargo == "gerente":
    print(f"O novo salario é de R${c101} com uma diferença de R${dif1} do salario base.")
elif cargo == "engenheiro":
    print(f"O novo salario é de R${c102} com uma diferença de R${dif2} do salario base.")
elif cargo == "tecnico":
    print(f"O novo salario é de R${c103} com uma diferença de R${dif3} do salario base.")
else:
    print(f"O novo salario é de R${c104} com uma diferença de R${dif4} do salario base.")