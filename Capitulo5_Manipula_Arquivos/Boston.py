with open("economic-indicators.csv", "r") as boston:
    total = 0
    maior = 0
    total_passageiros = 0
    for linha in boston.readlines()[1:-1]:
        total += int(linha.split(",")[3])
    print("O total de voos é: ", total)
    lista_passageiros = {}
    for linha in boston.readlines()[1:-1]:
        lista_passageiros[(linha.split(",")[0], linha.split(",")[1])]: linha.split(",")[2]

    for dados in lista_passageiros.values():
        valor_maximo = max(lista_passageiros.values())
        data_valor_maximo = lista_passageiros.keys()
    print("O valor máximo de passageiros data de: ", data_valor_maximo)
