from Capitulo3_Funcoes.IdentificacaoDeFuncoes import *

minhaLista = []
novaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 0.2)

print("Excluindo")
excluirPorSerial(minhaLista, novaLista)
exibirInventario(novaLista)

print("Resumindo")
resumirValores(novaLista)
