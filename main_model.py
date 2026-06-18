import requests
import os
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import calendar
from time import sleep

def options():
    print("1. Iniciar programa\n"
          "2. Cadastrar cidade nova\n"
          "3. Gráfico de temperatura\n"
          "4. Sair\n")
    

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

def buscar_coordenadas(nome_cidade):
    #Busca a latitude, longitude e timezone de qualquer cidade
    url_geo = f"https://geocoding-api.open-meteo.com/v1/search?name={nome_cidade}&count=1&language=pt&format=json"
    resposta = requests.get(url_geo).json()
    
    if "results" in resposta:
        cidade = resposta["results"][0]
        return {
            "lat": cidade["latitude"],
            "lon": cidade["longitude"],
            "nome": f"{cidade['name']}, {cidade.get('admin1', '')} - {cidade.get('country', '')}",
            "timezone": cidade["timezone"]
        }
    return None

def exibir_grafico_historico():
    print("=== CONSULTA DE HISTÓRICO CLIMÁTICO ===")
    cidade_input = input("Digite o nome da cidade (Ex: Arapiraca): ")

    localizacao = buscar_coordenadas(cidade_input)

    if not localizacao:
        print("Cidade não encontrada. Verifique a grafia e tente novamente.")
        return # Interrompe a função e volta pro menu

    print(f"Encontrado: {localizacao['nome']}")
    
    try:
        ano = int(input("Digite o ano (Ex: 2025): "))
        mes = int(input("Digite o mês (Ex: 1 para Janeiro, 5 para Maio): "))
        
        # OTIMIZAÇÃO: A biblioteca calendar descobre o último dia do mês automaticamente (incluindo bissextos)
        ultimo_dia = calendar.monthrange(ano, mes)[1]
        
        # O ":02d" formata números como 5 para "05" automaticamente
        start_date = f"{ano}-{mes:02d}-01"
        end_date = f"{ano}-{mes:02d}-{ultimo_dia}"
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos para ano e mês.")
        return

    url_historico = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": localizacao["lat"],
        "longitude": localizacao["lon"],
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": localizacao["timezone"]
    }

    print(f"\nBuscando dados entre {start_date} e {end_date}...")
    
    try:
        resposta = requests.get(url_historico, params=params)
        resposta.raise_for_status() # Checa se a resposta HTTP teve sucesso (200 OK)
        dados = resposta.json()
        
        # Cria o DataFrame
        df = pd.DataFrame({
            "Data": dados["daily"]["time"],
            "Máxima": dados["daily"]["temperature_2m_max"],
            "Mínima": dados["daily"]["temperature_2m_min"]
        })
        
        print("\n--- DADOS REPRODUZIDOS ---")
        print(df.to_string(index=False))
        
        # --- PLOTAGEM DO GRÁFICO ---
        plt.figure(figsize=(12, 6))
        plt.plot(df['Data'], df['Máxima'], label='Temp Máxima (°C)', color='darkorange', marker='o')
        plt.plot(df['Data'], df['Mínima'], label='Temp Mínima (°C)', color='teal', marker='o')
        
        plt.title(f'Histórico de Temperaturas - {localizacao["nome"]} ({mes:02d}/{ano})')
        plt.xlabel('Dias do Mês')
        plt.ylabel('Temperatura (°C)')
        
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()
        
        print("\n Abrindo o gráfico na tela...")
        sleep(2)
        clear()
        plt.show()
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar histórico de clima na API.")
        sleep(2)
        clear()

clear()

#Criação do json (caso ainda não tenha o arquivo)
file = Path("dados.json")
if file.exists() == False:
    os.system("touch dados.json")

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
    elif escolha == 3:
        clear()
        exibir_grafico_historico()
    elif escolha == 4:
        print("Saindo do programa...")
        exit()
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
