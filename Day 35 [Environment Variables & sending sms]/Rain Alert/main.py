import requests

# API_KEY = "f741f1b3e2b81d20523ab9fd11672cfa"
#
# parameters = {
#     "lat": 30.044420,
#     "lon": 31.235712,
#     "appid": API_KEY,
#     "exclude":"daily,minutely"
# }
#
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][0:12]
# for hour_data in weather_slice["weather"][0]["id"]:
import os
from twilio.rest import Client


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+14847598097',
                              to='+201050071610'
                          )

print(message.sid)
