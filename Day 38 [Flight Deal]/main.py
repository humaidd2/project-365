# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
from data_manager import DataManager
import requests
from datetime import datetime, timedelta
from flight_search import FlightSearch

sheety_url = ""
sheet_data = requests.get(url=sheety_url).json()
print(sheet_data)
data_manager = DataManager(sheet_data=sheet_data).update_sheet()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data["sheet1"]:
    flight = FlightSearch().check_flights(
        "CAI",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

