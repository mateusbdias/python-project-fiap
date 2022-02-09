ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo IPs: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa_end = input("Digite os dois últimos octetos: ")
print("Máquinas no mesmo endereço (redes diferentes)")
for ip, nome in ips.items():
    if ip[1] == pesquisa_end:
        print(nome)

print("Exibindo máquinas na mesma rede: ")
pesquisa_rede = input("Digite os dois primeiros octetos: ")
print("Máquinas na mesma rede (endereços diferentes)")
for ip, nome in ips.items():
    if ip[0] == pesquisa_rede:
        print(nome)
