import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=22.31&longitude=73.19&hourly=temperature_2m&past_days=7&timezone=auto"

response = requests.get(url).json()

hours = response['hourly']['time']
temperatures = response['hourly']['temperature_2m']

with open('Temperature.csv', 'w') as file:
    file.write("Time,Temperature\n")

    for i in range(168):
        file.write(f"{hours[i]},{temperatures[i]}\n")