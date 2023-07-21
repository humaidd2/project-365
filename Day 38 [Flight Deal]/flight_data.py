class FlightData:
    def __init__(self, price, lowest_price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.lowest_price = lowest_price
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
