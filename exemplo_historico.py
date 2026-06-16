import requests
import pandas as pd
import matplotlib.pyplot as plt

def buscar_coordenadas(nome_cidade):
    """Busca a latitude, longitude e timezone de qualquer cidade."""
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

# --- INPUTS DO USUÁRIO ---
print("=== CONSULTA DE HISTÓRICO CLIMÁTICO ===")
cidade_input = input("Digite o nome da cidade (Ex: Arapiraca): ")

# Busca os dados de localização da cidade digitada
localizacao = buscar_coordenadas(cidade_input)

if not localizacao:
    print("❌ Cidade não encontrada. Verifique a grafia e tente novamente.")
else:
    print(f"📍 Encontrado: {localizacao['nome']}")
    
    ano = input("Digite o ano (Ex: 2025): ")
    mes = input("Digite o mês com dois dígitos (Ex: 01 para Janeiro, 05 para Maio): ")
    
    # Validação simples de dias do mês
    if mes in ['01', '03', '05', '07', '08', '10', '12']:
        ultimo_dia = "31"
    elif mes in ['04', '06', '09', '11']:
        ultimo_dia = "30"
    else:
        # Fevereiro (considerando bissexto de forma simples)
        ultimo_dia = "29" if int(ano) % 4 == 0 else "28"
        
    start_date = f"{ano}-{mes}-01"
    end_date = f"{ano}-{mes}-{ultimo_dia}"

    # --- REQUISIÇÃO DA API DE HISTÓRICO ---
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
    resposta = requests.get(url_historico, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Cria o DataFrame
        df = pd.DataFrame({
            "Data": dados["daily"]["time"],
            "Máxima": dados["daily"]["temperature_2m_max"],
            "Mínima": dados["daily"]["temperature_2m_min"]
        })
        
        # Exibe os dados formatados no terminal
        print("\n--- DADOS REPRODUZIDOS ---")
        print(df.to_string(index=False))
        
        # --- PLOTAGEM DO GRÁFICO ---
        plt.figure(figsize=(12, 6))
        plt.plot(df['Data'], df['Máxima'], label='Temp Máxima (°C)', color='darkorange', marker='o')
        plt.plot(df['Data'], df['Mínima'], label='Temp Mínima (°C)', color='teal', marker='o')
        
        plt.title(f'Histórico de Temperaturas - {localizacao["nome"]} ({mes}/{ano})')
        plt.xlabel('Dias do Mês')
        plt.ylabel('Temperatura (°C)')
        
        # Ajusta os limites dos eixos para não cortar os nomes dos dias
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()
        
        print("\n🎨 Abrindo o gráfico na tela...")
        plt.show()
    else:
        print(f"❌ Erro ao buscar histórico de clima (Código: {resposta.status_code})")
        