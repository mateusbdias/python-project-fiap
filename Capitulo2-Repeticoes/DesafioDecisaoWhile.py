resposta = "SIM"
while resposta == "SIM":
    nivelAcesso = input("Digite o nível de acesso: ")
    genero = input("Digite o gênero: ")

    if nivelAcesso == "ADM":
        if genero == "F":
            print("Olá administradora")
        else:
            print("Olá administrador")
    elif nivelAcesso == "USR":
        if genero == "F":
            print("Olá usuária")
        else:
            print("Olá usuário")
    elif nivelAcesso == "GUEST":
        print("Olá visitante")
    else:
        if genero == "F":
            print("Olá desconhecida")
        else:
            print("Olá desconhecido")
    resposta = input("Digite SIM para continuar: ").upper()