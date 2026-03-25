print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
opcao_jogador1 = int(input("Jogador 1, escolha sua opção (1, 2 ou 3): "))
opcao_jogador2 = int(input("Jogador 2, escolha sua opção (1, 2 ou 3): "))
if opcao_jogador1 == opcao_jogador2:
    print("Empate!")
elif (opcao_jogador1 == 1 and opcao_jogador2 == 3) or (opcao_jogador1 == 2 and opcao_jogador2 == 1) or (opcao_jogador1 == 3 and opcao_jogador2 == 2):
    print("Jogador 1 vence!")
else:
    print("Jogador 2 vence!")