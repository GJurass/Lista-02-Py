vini = float(input("Digite o valor do produto:\n"))

pgto = int(input("Como sera efetuado o pagamento:\n"
                 "1- À vista em dinheiro ou cheque.\n"
                 "2- À vista no cartão de crédito.\n"
                 "3- Em 2 vezes.\n"
                 "4- Em 3 vezes.\n"))

f1 = vini * 0.9
f2 = vini * 0.85
f3 = vini / 2
f4 = (vini * 1.1) / 3

if pgto == 1:
    print("Valor a pagar R${:.2f}".format(f1))
elif pgto == 2:
    print("Valor a pagar R${:.2f}".format(f2))
elif pgto == 3:
    print("Valor da parcela (1/2) R${:.2f}".format(f3))
elif pgto == 4:
    print("Valor da parcela (1/3) R${:.2f}".format(f4))
else:
    print("Metodo de pagamento nao reconhecido.")