valor = float(input("Digite o valor de tabela do carro:\n"))
ano = int(input("Digite o ano de fabricação do carro:\n"))

bvalor = (valor * 1.01) - valor
avalor = (valor * 1.015) - valor

if ano <= 1990:
    print(f"O imposto a ser pago é de R${bvalor:.2f}")
elif ano > 1990:
    print(f"O imposto a ser pago é de R${avalor:.2f}")
