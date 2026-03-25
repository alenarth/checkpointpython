print("Sistema de aprovação escolar")
nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))
faltas = float(input("Digite a porcentagem de faltas: "))

media = (nota1 + nota2) / 2

if faltas > 25:
    print("Aluno reprovado por faltas.")
elif media >= 7:
    print("Aluno aprovado.")
elif media >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado por nota.")