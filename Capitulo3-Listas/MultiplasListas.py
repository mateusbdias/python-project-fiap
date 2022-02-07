equipamentos = []
valores = []
numerosSeriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numerosSeriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento " + str(indice + 1))
    print("Nome.........: " + equipamentos[indice])
    print("Valor........: " + str(valores[indice]))
    print("Número Serial: " + str(numerosSeriais[indice]))
    print("Departamento.: " + departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor........: " + str(valores[indice]))
        print("Número Serial: " + str(numerosSeriais[indice]))
        print("Departamento.: " + departamentos[indice])