import requests

api_key = "04ce4e5dc7a22dec89f84f92f42ea320"

city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]  # Temperature in Celsius (thanks to units=metric)
    humidity = data["main"]["humidity"]  # Humidity in percentage
    description = data["weather"][0]["description"]  # Weather condition (e.g., "clear sky")

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print(f"Oops! Something went wrong. Error code: {response.status_code}")
    print("Check your API key or city name!")