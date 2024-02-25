class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data):

        self.departure_city = flight_data["cityFrom"]
        self.departure_airport_code = flight_data["flyFrom"]
        self.departure_date = flight_data["local_departure"].split("T")[0]

        self.arrival_city = flight_data["cityTo"]
        self.arrival_airport_code = flight_data["flyTo"]
        self.arrival_data = flight_data["local_arrival"].split("T")[0]

        self.price = flight_data["price"]
