import os
import sys
import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: API_KEY environment variable is not set")
        sys.exit(1)

    city = os.getenv("CITY", "Paris")

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching weather data:", response.text)
        sys.exit(1)

    data = response.json()

    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")


if __name__ == "__main__":
    get_weather()
