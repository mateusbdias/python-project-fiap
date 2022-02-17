import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="wazeyes")

latitude = float(input("Digite a latitude...: "))
longitude = float(input("Digite a longitude.: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
if resultado[0] != 'None':
    print("Endereço completo.: ", resultado)
    print("Dado 1............: ", resultado[0])
    print("Dado 2............: ", resultado[1])
    print("Dado 3............: ", resultado[2])
