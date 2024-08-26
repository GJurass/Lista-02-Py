id = int(input("Digite seu numero de identificacao:\n"))

P1 = float(input("Digite a nota da P1\n"))
P2 = float(input("Digite a nota da P2\n"))
P3 = float(input("Digite a nota da P3\n"))

media = (P1 + P2 + P3) / 3

if media >= 7:
    print(f"O aluno {id} esta aprovado =)")
elif media < 7 and media >= 3:
    print(f"O aluno {id} precisara de recuperacao =/")
else:
    print(f"O aluno {id} esta reprovado =(")