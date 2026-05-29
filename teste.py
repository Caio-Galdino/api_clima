import requests

# Coordenadas de exemplo (São Paulo: Latitude -23.55, Longitude -46.63)
url = "https://api.open-meteo.com/v1/forecast?latitude=-9.751&longitude=-36.660&current_weather=true"

response = requests.get(url)
dados = response.json()

# Extraindo a temperatura atual
temperatura = dados["current_weather"]["temperature"]
print(f"A temperatura atual em arapiraca é: {temperatura}°C")

'''
coordenadas_cidades_brasil = [
    # --- REGIONAL NORDESTE ---
    
    # Alagoas
    {"cidade": "Maceió", "latitude": -9.665, "longitude": -35.735},
    {"cidade": "Arapiraca", "latitude": -9.751, "longitude": -36.660},
    {"cidade": "Maragogi", "latitude": -9.012, "longitude": -35.221},
    
    # Bahia
    {"cidade": "Salvador", "latitude": -12.971, "longitude": -38.501},
    {"cidade": "Feira de Santana", "latitude": -12.266, "longitude": -38.957},
    {"cidade": "Vitória da Conquista", "latitude": -14.866, "longitude": -40.838},
    
    # Ceará
    {"cidade": "Fortaleza", "latitude": -3.731, "longitude": -38.526},
    {"cidade": "Juazeiro do Norte", "latitude": -7.211, "longitude": -39.314},
    {"cidade": "Sobral", "latitude": -3.685, "longitude": -40.349},
    
    # Maranhão
    {"cidade": "São Luís", "latitude": -2.530, "longitude": -44.302},
    {"cidade": "Imperatriz", "latitude": -5.526, "longitude": -47.481},
    {"cidade": "Caxias", "latitude": -4.861, "longitude": -43.355},
    
    # Paraíba
    {"cidade": "João Pessoa", "latitude": -7.115, "longitude": -34.863},
    {"cidade": "Campina Grande", "latitude": -7.224, "longitude": -35.881},
    {"cidade": "Patos", "latitude": -7.024, "longitude": -37.275},
    
    # Pernambuco
    {"cidade": "Recife", "latitude": -8.054, "longitude": -34.877},
    {"cidade": "Jaboatão dos Guararapes", "latitude": -8.109, "longitude": -35.010},
    {"cidade": "Caruaru", "latitude": -8.283, "longitude": -35.971},
    
    # Piauí
    {"cidade": "Teresina", "latitude": -5.091, "longitude": -42.803},
    {"cidade": "Parnaíba", "latitude": -2.916, "longitude": -41.776},
    {"cidade": "Picos", "latitude": -7.081, "longitude": -41.467},
    
    # Rio Grande do Norte
    {"cidade": "Natal", "latitude": -5.794, "longitude": -35.209},
    {"cidade": "Mossoró", "latitude": -5.187, "longitude": -37.343},
    {"cidade": "Parnamirim", "latitude": -5.915, "longitude": -35.262},
    
    # Sergipe
    {"cidade": "Aracaju", "latitude": -10.911, "longitude": -37.073},
    {"cidade": "Nossa Senhora do Socorro", "latitude": -10.856, "longitude": -37.125},
    {"cidade": "Lagarto", "latitude": -10.917, "longitude": -37.650},

    # --- REGIÃO SUDESTE ---
    
    # Espírito Santo
    {"cidade": "Vitória", "latitude": -20.315, "longitude": -40.307},
    {"cidade": "Vila Velha", "latitude": -20.329, "longitude": -40.291},
    {"cidade": "Serra", "latitude": -20.128, "longitude": -40.312},
    
    # Minas Gerais
    {"cidade": "Belo Horizonte", "latitude": -19.920, "longitude": -43.935},
    {"cidade": "Uberlândia", "latitude": -18.918, "longitude": -48.277},
    {"cidade": "Contagem", "latitude": -19.932, "longitude": -44.052},
    
    # Rio de Janeiro
    {"cidade": "Rio de Janeiro", "latitude": -22.906, "longitude": -43.172},
    {"cidade": "Duque de Caxias", "latitude": -22.785, "longitude": -43.314},
    {"cidade": "São Gonçalo", "latitude": -22.826, "longitude": -43.047},
    
    # São Paulo
    {"cidade": "São Paulo", "latitude": -23.550, "longitude": -46.633},
    {"cidade": "Campinas", "latitude": -22.905, "longitude": -47.060},
    {"cidade": "Guarulhos", "latitude": -23.462, "longitude": -46.533},

    # --- REGIÃO SUL ---
    
    # Paraná
    {"cidade": "Curitiba", "latitude": -25.429, "longitude": -49.273},
    {"cidade": "Londrina", "latitude": -23.310, "longitude": -51.155},
    {"cidade": "Maringá", "latitude": -23.420, "longitude": -51.933},
    
    # Rio Grande do Sul
    {"cidade": "Porto Alegre", "latitude": -30.034, "longitude": -51.228},
    {"cidade": "Caxias do Sul", "latitude": -29.168, "longitude": -51.179},
    {"cidade": "Canoas", "latitude": -29.918, "longitude": -51.179},
    
    # Santa Catarina
    {"cidade": "Joinville", "latitude": -26.304, "longitude": -48.845},
    {"cidade": "Florianópolis", "latitude": -27.595, "longitude": -48.547},
    {"cidade": "Blumenau", "latitude": -26.919, "longitude": -49.066},

    # --- REGIÃO CENTRO-OESTE ---
    
    # Goiás
    {"cidade": "Goiânia", "latitude": -16.686, "longitude": -49.255},
    {"cidade": "Aparecida de Goiânia", "latitude": -16.823, "longitude": -49.246},
    {"cidade": "Anápolis", "latitude": -16.326, "longitude": -48.952},
    
    # Mato Grosso
    {"cidade": "Cuiabá", "latitude": -15.601, "longitude": -56.096},
    {"cidade": "Várzea Grande", "latitude": -15.646, "longitude": -56.132},
    {"cidade": "Rondonópolis", "latitude": -16.467, "longitude": -54.635},
    
    # Mato Grosso do Sul
    {"cidade": "Campo Grande", "latitude": -20.442, "longitude": -54.620},
    {"cidade": "Dourados", "latitude": -22.223, "longitude": -54.805},
    {"cidade": "Três Lagoas", "latitude": -20.788, "longitude": -51.701},

    # --- REGIÃO NORTE ---
    
    # Acre
    {"cidade": "Rio Branco", "latitude": -9.974, "longitude": -67.810},
    {"cidade": "Cruzeiro do Sul", "latitude": -7.631, "longitude": -72.673},
    {"cidade": "Sena Madureira", "latitude": -9.065, "longitude": -68.656},
    
    # Amapá
    {"cidade": "Macapá", "latitude": 0.034, "longitude": -51.066},
    {"cidade": "Santana", "latitude": -0.058, "longitude": -51.181},
    {"cidade": "Laranjal do Jari", "latitude": -0.842, "longitude": -52.513},
    
    # Amazonas
    {"cidade": "Manaus", "latitude": -3.119, "longitude": -60.021},
    {"cidade": "Parintins", "latitude": -2.628, "longitude": -56.786},
    {"cidade": "Itacoatiara", "latitude": -3.143, "longitude": -58.444},
    
    # Pará
    {"cidade": "Belém", "latitude": -1.455, "longitude": -48.490},
    {"cidade": "Ananindeua", "latitude": -1.365, "longitude": -48.379},
    {"cidade": "Santarém", "latitude": -2.443, "longitude": -54.699},
    
    # Rondônia
    {"cidade": "Porto Velho", "latitude": -8.761, "longitude": -63.903},
    {"cidade": "Ji-Paraná", "latitude": -10.880, "longitude": -61.895},
    {"cidade": "Ariquemes", "latitude": -9.913, "longitude": -63.029},
    
    # Roraima
    {"cidade": "Boa Vista", "latitude": 2.819, "longitude": -60.673},
    {"cidade": "Rorainópolis", "latitude": 0.948, "longitude": -60.413},
    {"cidade": "Caracaraí", "latitude": 1.817, "longitude": -61.127},
    
    # Tocantins
    {"cidade": "Palmas", "latitude": -10.167, "longitude": -48.329},
    {"cidade": "Araguaína", "latitude": -7.192, "longitude": -48.207},
    {"cidade": "Gurupi", "latitude": -11.729, "longitude": -49.067}
]
'''
