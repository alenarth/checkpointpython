print("Classificador de Meses e Dias")
numero_mes = int(input("Digite um número inteiro de 1 a 12: "))
match numero_mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("O mês tem 31 dias.")
    case 4 | 6 | 9 | 11:
        print("O mês tem 30 dias.")
    case 2:
        print("O mês tem 28 ou 29 dias (fevereiro).")
    case _:
        print("Número inválido. Por favor, digite um número entre 1 e 12.")