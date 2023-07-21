from twilio.rest import Client
import requests
from flight_data import FlightData

account_sid = ""
auth_token = ""
sheety_url = ""
sheet_data = requests.get(url=sheety_url).json()
flight_data = FlightData()


class NotificationManager:

    def check_if_lower(self):
        for data in sheet_data["sheet1"]:
            lowestprice = data["lowestPrice"]
            if FlightData().price > lowestprice:
                self.sendmessage()

    def sendmessage(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Low Price Alert! Only{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to "
                 f"{flight_data.destination_city}-{flight_data.destination_airport} "
                 f"from {flight_data.out_date} to {flight_data.return_date} ",
            from_='+14847598097',
            to='+201050071610'
        )
