''' AINDA FALTA ENCONTRAR UM JEITO DE CATALOGAR -CIDADE,LATITUDE,LONGITUDE-
    CRIAR ARQUIVO CUJO NOME SEJA O DA CIDADE, E DENTRO DELE PÔR UMA LISTA
    COM AS DUAS COORDENADAS DA CIDADE. DEPOIS AUTOMATIZAR O PROCESSO
    DE CRIAÇÃO DO ARQUIVO + LISTA, E DE ESCOLHA DA CIDADE DENTRO DO WHILE'''

import requests
import os

#FUNÇÃO DE LIMPEZA DO TERMINAL
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

#CRIAÇÃO DE ARQUIVO PARA ARMAZENAR DADOS
while True:
    cidade = input("Digite o nome da cidade: ")
    if os.path.exists("Cidades") == False:
        os.mkdir("Cidades")

        path = os.path.join("Cidades", f"{cidade}.py")

        latitude = input("Digite a latitude: ")
        longitude = input("Digite a longitude: ")
        with open(path, "w") as f:
            f.write(f'coord1 = ["{latitude}"]\n')
            f.write(f'coord2 = ["{longitude}"]\n')
        break
    else:
        break
        
''' ERRO NO URL, DIZ QUE NÃO FOI DEFINIDO.
    ENTENDER POR QUE NÃO PASSA PELA VERIFICAÇÃO
    DO WHILE ACIMA '''

#CONEXÃO DA API COM O SITE
url = f"https://api.open-meteo.com/v1/forecast?latitude={coord1[0]}&longitude={coord2[0]}&current_weather=true"
try:
    response = requests.get(url)
    dados = response.json()
    temperatura = dados["current_weather"]["temperature"]
    clear()
    print(f"A temperatura atual em {cidade} é: {temperatura}°C")
    loop = input("Gostaria de continuar o programa? S/N\n").upper()
    #LOOP PRA CONSERTAR, DEIXA O PROGRAMA LIGADO
    if loop == "S":
        clear()
        continue
    else:
        clear()
        break
except Exception:
    print("Dados não encontrados.")
    break
