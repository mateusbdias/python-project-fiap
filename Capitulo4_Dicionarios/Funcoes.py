def perguntar():
    resposta = input("Selecione uma opção: \n'I' para inserir um usuário\n'P' "
                     "para pesquisar um usuário\n'E' para excluir um usuário\n"
                     "'L' para listar os usuários\nOpção: ").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o código: ")
    dicionario[chave] = [
        input("Digite o login: "),
        input("Digite o nome: "),
        input("Digite a data de acesso: "),
        input("Digite a hora de acesso: "),
        input("Digite a estação acessada: "),
        input("Digite o nível do usuário: ")
    ]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Login..........: " + lista[0])
        print("Nome...........: " + lista[1])
        print("Data de acesso.: " + lista[2])
        print("Hora de acesso.: " + lista[3])
        print("Estação........: " + lista[4])
        print("Nível..........: " + lista[5])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Objeto excluído")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Código:", chave)
        print("Dados:", valor)
