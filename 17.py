codigo = int(input("Digite um código de erro HTTP comum (200, 400, 401, 403, 404, 500): "))
match codigo:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Código de erro inválido ou não cadastrado.")