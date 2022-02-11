from Funcoes.Funcoes_JSON import *

inventario = lerArquivo("inventario_json.json")
opcao = chamarMenu()
while 0 < opcao < 3:
    if opcao == 1:
        registrarAtivo(inventario, "inventario_json.json")
    elif opcao == 2:
        exibirAtivos("inventario_json.json")
    opcao = chamarMenu()
