print("Conversor de Moedas")
valor_reais = float(input("Digite o valor em Reais (R$): "))
print("Escolha a moeda alvo:")
print("1 - Dólar (USD)")
print("2 - Euro (EUR)")
print("3 - Libra (GBP)")
print("4 - Iene (JPY)")
escolha = int(input("Digite o número correspondente à moeda: "))
match escolha:
    case 1:
        taxa_cambio = 0.20
        moeda = "Dólar (USD)"
    case 2:
        taxa_cambio = 0.18
        moeda = "Euro (EUR)"
    case 3:
        taxa_cambio = 0.15
        moeda = "Libra (GBP)"
    case 4:
        taxa_cambio = 22.00
        moeda = "Iene (JPY)"
    case _:
        print("Opção inválida.")
        exit()
valor_convertido = valor_reais * taxa_cambio
print(f"{valor_reais:.2f} Reais equivalem a {valor_convertido:.2f} {moeda}.")
