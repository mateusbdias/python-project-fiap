from Funcoes.Funcoes_Dicionarios import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Digite a chave a ser pesquisada: "))
    if opcao == "E":
        excluir(usuarios, input("Digite a chave do objeto a ser excluído: "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
