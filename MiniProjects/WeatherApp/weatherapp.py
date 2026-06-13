import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    current = data["current_condition"][0]

    print(f"\nWeather in {city}")
    print(f"Temperature : {current['temp_C']}°C")
    print(f"Humidity    : {current['humidity']}%")
    print(f"Condition   : {current['weatherDesc'][0]['value']}")
    print(f"Wind Speed  : {current['windspeedKmph']} km/h")

except Exception as e:
    print("Error:", e)