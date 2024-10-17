import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    weather = get_weather(city, api_key)

    if weather.get("cod") != 200:
        print("City not found!")
    else:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['main']['temp']}°C")
        print(f"Weather: {weather['weather'][0]['description']}")

if __name__ == "__main__":
    main()
