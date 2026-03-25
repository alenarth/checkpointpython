print("Calculadora Segura")
num1 = float(input("Digite o primeiro número decimal: "))
num2 = float(input("Digite o segundo número decimal: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, *, /.")