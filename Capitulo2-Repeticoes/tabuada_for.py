numero = int(input("Digite um número: "))
print("Tabuada do número " + str(numero))
for valor in range(1, 11, 1):
    print(" " + str(numero) + " x " + str(valor) + " = " + str(numero * valor))
