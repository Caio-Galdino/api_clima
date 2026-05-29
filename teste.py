import requests

# Coordenadas de exemplo (São Paulo: Latitude -23.55, Longitude -46.63)
url = "https://api.open-meteo.com/v1/forecast?latitude=-9.751&longitude=-36.660&current_weather=true"

response = requests.get(url)
dados = response.json()

# Extraindo a temperatura atual
temperatura = dados["current_weather"]["temperature"]
print(f"A temperatura atual em arapiraca é: {temperatura}°C")
