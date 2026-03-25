print("Sistema de Descontos e Juros")
valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Escolha a forma de pagamento\n1 - À vista no PIX\n2 - Cartão de crédito 1x\n3 - Cartão de crédito parcelado\n"))
if forma_pagamento == 1:
    valor_final = valor_produto * 0.90  # 10% de desconto
    print(f"Valor final com desconto para PIX: R${valor_final:.2f}")
elif forma_pagamento == 2:
    valor_final = valor_produto  # preço original
    print(f"Valor final para Cartão de crédito 1x: R${valor_final:.2f}")
elif forma_pagamento == 3:
    valor_final = valor_produto * 1.05  # 5% de juros
    print(f"Valor final com juros para parcelamento: R${valor_final:.2f}")
else:
    print("Opção de pagamento inválida. Por favor, escolha 1, 2 ou 3.")
    