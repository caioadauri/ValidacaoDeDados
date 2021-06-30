import requests
from acesso_cep import BuscaEndereco

cep = "04071045"
object_cep = BuscaEndereco(cep)


#r = requests.get("https://viacep.com.br/ws/04071045/json/")
#print(r.text)

bairro, cidade, uf = object_cep.acessa_via_cep()
print(bairro, cidade, uf)