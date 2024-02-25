import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = "https://api.sheety.co/e65846ffb81dcf1ea9b329dfe8498ebc/flightDeals"
        self.auth = {"Authorization": "Bearer 981280"}

    def get_price_data(self):
        url = f"{self.sheet_url}/prices"
        response = requests.get(url=url, headers=self.auth)
        # print("get_data response", response)
        response.raise_for_status()
        return response.json()["prices"]

    def put_price_data(self, row_id, code):
        url = f"{self.sheet_url}/prices/{row_id}"
        body = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=url, json=body, headers=self.auth)
        response.raise_for_status()

    def check_email(self, email):
        url = f"{self.sheet_url}/users"
        response = requests.get(url=url, headers=self.auth)
        users = response.json()["users"]

        for user in users:
            if user["emailId"] == email:
                return True
        return False

    def post_user_data(self, first_name, last_name, email_id):
        url = f"{self.sheet_url}/users"
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "emailId": email_id,
            }
        }
        r = requests.post(url=url, json=body, headers=self.auth)
        r.raise_for_status()
