# Professor Cainã. Obrigado por compartilhar o conhecimento com a gente. Você é um excelente professor, e os exercícios apesar de simples, com certeza ajudam a fixar o conteúdo.
# Conte comigo também para auxiliar a galera, caso alguém tenha dúvidas!

print("Sistema de Pedágio")
tipo_veiculo = input("Digite o tipo de veículo (carro, moto, onibus, caminhao): ").lower()
match tipo_veiculo:
    case "carro":
        valor_pedagio = 10.00
        print(f"O valor do pedágio para carro é R$ {valor_pedagio:.2f}.")
    case "moto":
        valor_pedagio = 5.00
        print(f"O valor do pedágio para moto é R$ {valor_pedagio:.2f}.")
    case "onibus":
        valor_pedagio = 20.00
        print(f"O valor do pedágio para ônibus é R$ {valor_pedagio:.2f}.")
    case "caminhao":
        quantidade_eixos = int(input("Digite a quantidade de eixos do caminhão: "))
        if quantidade_eixos <= 2:
            valor_pedagio = 30.00
        else:
            valor_pedagio = 30.00 + (quantidade_eixos - 2) * 5.00
        print(f"O valor do pedágio para caminhão com {quantidade_eixos} eixos é R$ {valor_pedagio:.2f}.")
    case _:
        print("Tipo de veículo inválido. Por favor, digite 'carro', 'moto', 'onibus' ou 'caminhao'.")