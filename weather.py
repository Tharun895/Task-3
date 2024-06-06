import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather_data(weather_data):
    if weather_data.get('cod') != 200:
        print(f"Error: {weather_data.get('message')}")
        return

    main = weather_data['main']
    weather = weather_data['weather'][0]

    print(f"City: {weather_data['name']}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Weather: {weather['description'].title()}")


def main():
    api_key = "aa67a77495ddfb24fb0b96c7adc987f1"
    location = input("Enter the city name or ZIP code: ")

    weather_data = get_weather_data(api_key, location)
    display_weather_data(weather_data)

if _name_ == "_main_":
    main()
