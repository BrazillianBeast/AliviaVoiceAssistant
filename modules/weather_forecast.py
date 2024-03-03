import requests
import json
# import response_current_conditions

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def get_weather():


    # Insira sua chave de API do OpenWeatherMap aqui
    API_KEY = '8X6V3C9Y662UNVUZM4Q63PABA'
    # Insira o nome da cidade e o código do país (se necessário)
    # city = 'Sao Paulo'
    # country_code = 'BR'
    # Monta a URL da API do OpenWeatherMap
    url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/S%C3%A3o%20bernardo%20do%20campo?unitGroup=metric&include=current&key={API_KEY}&contentType=json'
    
    # Faz a solicitação GET para a API
    raw_response = requests.get(url)
    # response = response_current_conditions.main()
    # status_code = 200

    # Verifica se a solicitação foi bem-sucedida
    if raw_response.status_code == 200:
        response = raw_response.json()
        # Extrai a temperatura atual da resposta JSON
        # data = response.json()
        current_city_name = response['address']
        response_current_weather_celsius = int(response['currentConditions']['temp'])
        response_current_humidity = int(response['currentConditions']['humidity'])

        return(f'A temperatura em {current_city_name}: é de {response_current_weather_celsius} graus célsius, com umidade em: {response_current_humidity} porcento')
    else:
        print('Falha ao obter a temperatura.')

if __name__ == "__main__":
    get_weather('Sao Paulo')