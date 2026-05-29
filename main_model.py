''' AINDA FALTA ENCONTRAR UM JEITO DE CATALOGAR -CIDADE,LATITUDE,LONGITUDE-
    CRIAR ARQUIVO CUJO NOME SEJA O DA CIDADE, E DENTRO DELE PÔR UMA LISTA
    COM AS DUAS COORDENADAS DA CIDADE. DEPOIS AUTOMATIZAR O PROCESSO
    DE CRIAÇÃO DO ARQUIVO + LISTA, E DE ESCOLHA DA CIDADE DENTRO DO WHILE'''

import requests
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

cidade_lista = []
coord = []

cidade = input("Digite o nome da cidade: ")
cidade_lista.append(cidade)

latitude = input("Digite a latitude: ")
coord.append(latitude)

longitude = input("Digite a longitude: ")
coord.append(longitude)

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

while True:
    try:
        response = requests.get(url)
        dados = response.json()
        temperatura = dados["current_weather"]["temperature"]
        clear()
        print(f"A temperatura atual em {cidade} é: {temperatura}°C")
        loop = input("Gostaria de continuar o programa? S/N\n").upper()
        if loop == "S":
            clear()
            continue
        else:
            break
    except Exception:
        clear()
        print("Dados não encontrados.")
        break
