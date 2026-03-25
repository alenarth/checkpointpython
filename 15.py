# Professor Cainã, se você estive lendo isso, escreva "Qué ota no Teams"
print("Bem-vindo ao Caixa Eletrônico!")
valor_saque = int(input("Digite o valor do saque (número inteiro): "))
notas = [100, 50, 20, 10, 5, 2]
quantidade_notas = {}
if valor_saque < 2 or valor_saque % 2 != 0:
    print("Erro: O valor do saque deve ser um número inteiro maior ou igual a 2 e múltiplo de 2.")
else:
    for nota in notas:
        quantidade_notas[nota] = valor_saque // nota
        valor_saque = valor_saque % nota

    print("Notas entregues:")
    for nota, quantidade in quantidade_notas.items():
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${nota}")
        else:
            print(f"0 nota(s) de R${nota}")
