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
        cidade = input("Digite o nome da cidade (sem acentuação): ").upper()
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
for cidade in dados:
    if cidade["cidade"] == pull_city:
        cidade_encontrada = cidade
        latitude = cidade_encontrada["latitude"]
        longitude = cidade_encontrada["longitude"]
        break
    else:
        cidade_encontrada = cidade
        latitude = cidade_encontrada["latitude"]
        longitude = cidade_encontrada["longitude"]
    #Conexão com a API
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")

    response = requests.get(url)
    dados_api = response.json()

    temperatura = dados_api["current_weather"]["temperature"]
    clima = dados_api["current_weather"]["is_day"]
    if clima == 1:
        clima = "dia"
    else:
        clima = "noite"
    #Output de informações para o usuário
    print(
        f"A temperatura atual em {cidade_encontrada["cidade"]} é {temperatura}°C\n"
        f"No momento, {cidade_encontrada["cidade"]} está de {clima}.\n"
        )
    #Falta mostrar o clima atual (se ta chovendo ou fazendo sol)
