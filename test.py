import requests

url = "http://localhost:5001/process_weather"
data = {
    "temperature": 25,
    "humidity": 60,
    "weather_description": "Ramesh"
}

response = requests.post(url, json=data)

print(response.text)
