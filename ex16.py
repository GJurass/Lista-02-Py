saldm = float(input("Digite seu saldo medio do ultimo ano:\n"))

lv1 = saldm * 0.2
lv2 = saldm * 0.3
lv3 = saldm * 0.4

if saldm >= 0 and saldm <= 200:
    print(f"Nao sera liberado credito devido ao seu saldo medio atual de R${saldm}")
elif saldm > 200 and saldm <= 400:
    print(f"Sera liberado um credito de R${lv1} devido ao seu saldo medio atual de R${saldm}")
elif saldm > 400 and saldm <= 600:
    print(f"Sera liberado um credito de R${lv2} devido ao seu saldo medio atual de R${saldm}")
elif saldm > 600:
    print(f"Sera liberado um credito de R${lv3} devido ao seu saldo medio atual de R${saldm}")