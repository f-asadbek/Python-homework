import requests

class WeatherApp:
    def __init__(self, city_name):
        self.city_name = city_name
        self.api_key = "c2e02823bf32fc29cfc2505bce0578f8"
        self.base_api = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}&units=metric"
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.weather_description = None

    def fetch_weather(self):
        response = requests.get(self.base_api)
        if response.status_code == 200:
            data = response.json()
            self.temperature = data["main"]["temp"]
            self.humidity = data["main"]["humidity"]
            self.pressure = data["main"]["pressure"]
            self.weather_description = data["weather"][0]["description"]
        else:
            raise Exception("Invalid input or city not found!")

    def __str__(self):
        if self.temperature is not None:
            return f"Temperature: {self.temperature}°C \nHumidity: {self.humidity}% \nPressure: {self.pressure} hPa \nWeather description: {self.weather_description}"
        return "Weather data not available"

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather = WeatherApp(city_name)
    weather.fetch_weather()
    print(weather)
