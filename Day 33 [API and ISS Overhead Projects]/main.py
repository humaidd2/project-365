import requests
import datetime

# response = requests.get("http://api.open-notify.org/iss-now.json")
# data = response.json()["iss_position"]
#
# longitude = data["longitude"]
# latitude = data["latitude"]
# iss_location = (longitude, latitude)
#
# print(iss_location)

MY_LAT = 51.507351
MY_LNG = -0.127758


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)

now = datetime.datetime.now().hour
print(now)
