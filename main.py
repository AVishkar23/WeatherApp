import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=3"
weather = requests.get(url)
print(weather.text)
