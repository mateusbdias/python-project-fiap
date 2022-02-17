import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereco com número e cidade.\n"
                 "Exemplo: Avenida Paulista, 100, São Paulo: ")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0] != 'None':
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Região............: ", resultado[3])
