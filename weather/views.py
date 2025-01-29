from django.shortcuts import render
import requests
from django.conf import settings

def get_weather(city):
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    print("API Response:", response.json())
    if response.status_code == 200:
        return response.json()
    return None

def home(request):
    city = request.GET.get("city")
    weather_data = get_weather(city) if city else None

    print("Weather Data in Template:", weather_data)  # Debugging

    return render(request, "weather/home.html", {"weather": weather_data, "city": city})

