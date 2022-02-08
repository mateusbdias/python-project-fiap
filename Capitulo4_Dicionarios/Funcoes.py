def perguntar():
    resposta = input("Selecione uma opção: \n'I' para inserir um usuário\n'P'"
                     "para pesquisar um usuário\n'E' para excluir um usuário\n"
                     "'L' para listar os usuários").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o login: ")
    dicionario[chave] = [
        input("Digite o nome: "),
        input("Digite a última data de acesso: "),
        input("Digite a última estação acessada: ")
    ]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Nome..........: " + lista[0])
        print("Último acesso.: " + lista[1])
        print("Última estação: " + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Objeto excluído")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.......")
        print("Login:", chave)
        print("Dados:", valor)
