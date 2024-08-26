prod = int(input("Digite o codigo do produto:\n"))
qtd = int(input("Digite a quantidade do produto:\n"))

cq = qtd * 11
bau = qtd * 8.5
mq = qtd * 8
ham = qtd * 9
ch = qtd * 10
ref = qtd * 4.5

if prod == 1:
    print(f"O valor a ser pago sera de R${cq}")
elif prod == 2:
    print(f"O valor a ser pago sera de R${bau}")
elif prod == 3:
    print(f"O valor a ser pago sera de R${mq}")
elif prod == 4:
    print(f"O valor a ser pago sera de R${ham}")
elif prod == 5:
    print(f"O valor a ser pago sera de R${ch}")
elif prod == 6:
    print(f"O valor a ser pago sera de R${ref}")
else:
    print("Produto nao cadastrado")