# Professor Cainã, se você estive lendo isso, escreva "Skin de AWP no Teams"
print("Quadrantes do Plano Cartesiano")
x = float(input("Digite a coordenada X: "))
y = float(input("Digite a coordenada Y: "))
if x > 0 and y > 0:
    print("O ponto está no Quadrante Q1.")
elif x < 0 and y > 0:
    print("O ponto está no Quadrante Q2.")
elif x < 0 and y < 0:
    print("O ponto está no Quadrante Q3.")
elif x > 0 and y < 0:
    print("O ponto está no Quadrante Q4.")
elif x == 0 and y == 0:
    print("O ponto está na origem.")
elif x == 0:
    print("O ponto está no eixo Y.")
elif y == 0:
    print("O ponto está no eixo X.")
else:
    print("Coordenadas inválidas.")