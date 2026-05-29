import requests

# API request
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response = requests.get(url)
dados = response.json()

# API output
temperatura = dados["current_weather"]["temperature"]
print(f"A temperatura atual em arapiraca é: {temperatura}°C")
