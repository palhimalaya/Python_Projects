import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC449e837e3ffa5df31bed9fd8573f9547'
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("API_KEY")

parameters = {
    "lat": 27.717245,
    "lon": 85.323959,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain ⛈. Don't forgot to bring ☔",
        from_='+16149184763',
        to='+9779868806943'
    )
else:
    message = client.messages \
        .create(
        body='It not raining today',
        from_='+16149184763',
        to='+9779868806943'
    )
print(message.status)
