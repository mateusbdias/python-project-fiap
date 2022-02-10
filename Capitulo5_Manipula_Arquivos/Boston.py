with open("economic-indicators.csv", "r") as boston:
    total_voos = 0
    maior_passageiros = 0
    mes = 0
    ano = 0
    total_passageiros = 0
    maior_media_hotel = 0
    mes_maior_media = 0
    ano_pesquisa = input("Digite o ano a ser pesquisado: ")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        # Total de voos internacionais
        if lista[0] == ano_pesquisa:
            total_voos += int(lista[3])
        # Data do maior trânsito de passageiros
        if int(lista[2]) > int(maior_passageiros):
            maior_passageiros = int(lista[2])
            mes = lista[1]
            ano = lista[0]
        # Total de passageiros
        if lista[0] == ano_pesquisa:
            total_passageiros += int(lista[2])
        # Maior média da diária de hotel
        if lista[0] == ano_pesquisa:
            if float(lista[5]) > float(maior_media_hotel):
                maior_media_hotel = lista[5]
                mes_maior_media = lista[1]

    print("O total de voos no ano de " + str(ano_pesquisa) + " foi de: " +
          str(total_voos))
    print("O valor máximo de passageiros data de: " + str(mes) + "/" + str(ano))
    print("O total de passageiros no ano de " + str(ano_pesquisa) +
          " foi de " + str(total_passageiros))
    print("O mês com maior média da diária de hotel no ano de " +
          str(ano_pesquisa) + " foi: " + str(mes_maior_media))
