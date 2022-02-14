import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "71ee1bb5321997ffca9afd4da911f42b"

parameters = {
    "lat": 22.545538,
    "lon": 95.712393,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
        print("bring umbrella")

if will_rain:
    print("bring umbrella")
else:
    print("you can go out without umbrella")

