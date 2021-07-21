import requests
import os
from twilio.rest import Client

own_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "OWN_API_KEY"
MY_LAT = 12.971599
MY_LONG = 77.594566
account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"

# api_key = os.environ.get("OWN_API_KEY")
# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "exclude": "current,minutely,daily,alerts"
    }

response = requests.get(url= own_endpoint, params= parameters)
response.raise_for_status()

weather_data = response.json()
print(weather_data)
weather_slice = weather_data['hourly'][:12]
condition_code = [hourly["weather"][0]["id"] for hourly in weather_slice]


will_rain = False
for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to take an ☔️ while going out.",
        from_='+17603139117',
        to='+919972953907'
    )
    print(message.status)

# print(weather_data['hourly'][0]["weather"][0]["id"])

