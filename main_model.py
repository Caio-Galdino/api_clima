import requests
import os
import json

def options():
    print("1. Iniciar programa\n"
          "2. Cadastrar cidade nova\n")
    

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def busca(city, dados):
    index = -1
    for i in range(len(dados)):
        if(dados[i]['cidade'] == city):
            return i
    return -1

clear()

try:
    with open("dados.json", "r") as pull_city:
        dados = json.load(pull_city)
except:
    print("Erro.")

#Opções de ação (registrar novas coordenadas)
while True:
    options()
    escolha = int(input("Digite a opção desejada: "))
    #"Rodar o programa"
    if escolha == 1:
        clear()
        break
    #"Registrar nova cidade"
    elif escolha == 2:
        cidade = input("Digite o nome da cidade: ").upper()
        latitude = input("Digite a latitude: ")
        longitude = input("Digite a longitude: ")
        #Criação em arquivo JSON
        nova_cidade = {
            "cidade": cidade,
            "latitude": latitude,
            "longitude": longitude
            }
        try:
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)
        except:
            dados = []

        dados.append(nova_cidade)
        with open("dados.json", "w") as arquivo:
            json.dump(dados,arquivo,indent=4)
        clear()
    else:
        print("Inválido.")
        continue

#Busca as coordenadas das cidades no arquivo JSON 
cidade_encontrada = None
pull_city = input("Qual cidade? ").upper()
index = busca(pull_city, dados)
if (index > -1):
    cid = dados[index]
    print(cid["cidade"])
    print(cid["longitude"])
    print(cid["latitude"])

for cidade in dados:
    if cidade["cidade"] == pull_city:
        cidade_encontrada = cidade
        latitude = cidade_encontrada["latitude"]
        longitude = cidade_encontrada["longitude"]
        break

if cidade_encontrada is None:
    print("Cidade não encontrada. Faça o registro.")
    exit()
    #Conexão com a API
url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")

clear()
print("Trabalhando...")

response = requests.get(url)
dados_api = response.json()

clear()

temperatura = dados_api["current_weather"]["temperature"]
clima = dados_api["current_weather"]["is_day"]
clima = dados_api["current_weather"]["weathercode"]

#weathercode
if clima == 0:
    clima = "ensolarado"
elif clima in [1,2,3]:
    clima = "parcialmente nublado"
elif clima in [45,46,47,48]:
    clima = "com névoa"
elif clima in [51,52,53,54,55]:
    clima = "chuviscando"
elif clima in [61,63,65,95,96,97,98,99]:
    clima = "chovendo"
elif clima in [71,72,73,74,75,80,81,82,85,86]:
    clima = "nevando"
elif clima in [95,96,97,98,99]:
    clima = "trovejando"
    
#is_day
if dia == 1:
    dia = "dia"
else:
    dia = "noite"

#Output de informações para o usuário
print(
    f"A temperatura atual em {cidade_encontrada["cidade"]} é {temperatura}°C\n"
    f"No momento, {cidade_encontrada["cidade"]} está de {dia}, e está {clima}."
    )
