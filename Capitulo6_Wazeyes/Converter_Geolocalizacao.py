import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
from Funcoes.Funcoes_JSON import lerArquivo, gravarArquivo
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
dicionario = lerArquivo("entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + " " + lista[1] + " " + lista[3]
location = geolocator.geocode(endereco)
saida = {"coordenadas": (location.latitude, location.longitude)}
gravarArquivo(saida, "saida.json")
