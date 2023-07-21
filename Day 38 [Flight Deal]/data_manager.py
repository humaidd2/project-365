from flight_search import FlightSearch
import requests


class DataManager:

    def __init__(self, sheet_data):
        self.sheet_data = sheet_data

    def update_sheet(self):
        for data in self.sheet_data["sheet1"]:
            if data["iataCode"] == "":
                flight_search_response = FlightSearch().search_city_code(data["city"])
                object_id = data["id"]
                city = data["city"]
                price = data["lowestPrice"]
                sheety_put_url = f"{object_id}"
                body = {
                    "sheet1": {
                        "city": city,
                        "iataCode": flight_search_response,
                        "lowestPrice": price,
                    }
                }
                requests.put(sheety_put_url, json=body)
