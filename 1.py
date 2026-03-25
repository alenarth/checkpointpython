# Professor Cainã, se você estive lendo isso, escreva "Smoke no Janelão no Teams"
print("Calculadora de IMC Detalhada")
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))

altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III (mórbida)"
    

print(f"{nome}, seu IMC é: {imc:.2f}. Classificação: {classificacao}.")

