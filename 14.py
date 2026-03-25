print("Digite uma data para validação:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
def validar_data(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False
    return True
if validar_data(dia, mes, ano):
    print("A data é válida.")
else:    
    print("A data é inválida.")
    