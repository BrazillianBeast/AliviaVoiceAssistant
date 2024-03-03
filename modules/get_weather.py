
def get_weather(city):
    import requests
    # Insira sua chave de API do OpenWeatherMap aqui
    API_KEY = 'beb3f6c4dc883f0d3cbc4da969f1437f'
    # Insira o nome da cidade e o código do país (se necessário)
    city = 'Sao Paulo'
    country_code = 'BR'
    # Monta a URL da API do OpenWeatherMap
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}'
    # Faz a solicitação GET para a API
    response = requests.get(url)
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Extrai a temperatura atual da resposta JSON
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f'Temperatura em {city}: {temperature_celsius:.2f} °C')
    else:
        print('Falha ao obter a temperatura.')

if __name__ == "__main__":
    get_weather('Sao Paulo')