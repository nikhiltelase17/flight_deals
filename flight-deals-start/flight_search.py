import requests
import json


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = "https://api.tequila.kiwi.com"
        self.header = {'apikey': 'BohyoD5d-OWMVnSUtGnno9N_jIyUy12-'}

    def city_iata_code(self, city):
        location_url = f"{self.url}/locations/query?"
        parameter = {"term": city}

        response = requests.get(url=location_url, params=parameter, headers=self.header)
        response.raise_for_status()

        iata_code = response.json()["locations"][0]["code"]
        return iata_code

    def flight_data(self, fly_from, fly_to, date_from, date_to, nights_in_dst_from, nights_in_dst_to):
        search_url = f"{self.url}/v2/search?"
        parameter = {"fly_from": fly_from,
                     "fly_to": fly_to,
                     "date_from": date_from,
                     "date_to": date_to,
                     "nights_in_dst_from": nights_in_dst_from,
                     "nights_in_dst_to": nights_in_dst_to,
                     }
        response = requests.get(url=search_url, params=parameter, headers=self.header)
        with open("data.json", "w") as data:
            json.dump(response.json(),  data, indent=2)

        try:
            data = response.json()["data"][0]
            return data
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

