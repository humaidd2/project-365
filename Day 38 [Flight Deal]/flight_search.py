import requests
from flight_data import FlightData

APIKEY = ""
search_endpoint = ""
header = {
    "apikey": APIKEY
}


class FlightSearch:
    def search_city_code(self, city_name):
        api_url = f"https://api.tequila.kiwi.com/locations/query?term={city_name}&locale=en-US&active_only=true"

        response = requests.get(api_url, headers=header)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=search_endpoint, headers=header, params=params).json()

        for data in response["data"]:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0])
            return flight_data
