from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# -----------calculating tomorrow date and after 6month date-----------
now = datetime.now()
tomorrow = now + timedelta(days=1)
after_6month = now + timedelta(days=6*30)

# -------------flight data-----------------------
DATE_FROM = tomorrow.strftime("%d/%m/%Y")
DATE_TO = after_6month.strftime("%d/%m/%Y")
FLY_FROM = "LON"   # it's iata code of London
NIGHTS_IN_DST_FROM = 7
NIGHTS_IN_DST_TO = 28

# -------------crating class objects------------
data = DataManager()
search_flight = FlightSearch()
messanger = NotificationManager()

# -----------user input------------
# first_name = input("Enter your first name: ")
# second_name = input("Enter your second name: ")
# email = input("Enter your email address: ")
#
# # checking user email already in user_sheet data
# if data.check_email(email):
#     print("Your email already registered.😩😩 ")
# else:
#     data.post_user_data(first_name, second_name, email)
#     print("Your registration has successful.✅✅")


# ------------- getting price_sheet data, entering data, and sending message--------------
price_data = data.get_price_data()

for flight_deal in price_data:
    if flight_deal["iataCode"] == '':
        # getting city iata code
        flight_deal["iataCode"] = search_flight.city_iata_code(city=flight_deal["city"])
        data.put_price_data(row_id=flight_deal["id"], code=flight_deal["iataCode"])

    # getting flight data
    FLY_TO = flight_deal["iataCode"]
    search_flight_data = search_flight.flight_data(fly_from=FLY_FROM,
                                                   fly_to=FLY_TO,
                                                   date_from=DATE_FROM,
                                                   date_to=DATE_TO,
                                                   nights_in_dst_from=NIGHTS_IN_DST_FROM,
                                                   nights_in_dst_to=NIGHTS_IN_DST_TO,
                                                   )

    # passing search_flight_data into flight_data.py
    if not search_flight_data == None:
        flight = FlightData(flight_data=search_flight_data)

        # # sending message if flight price lower_than google sheet lowest_price
        if flight.price < flight_deal["lowestPrice"]:
            print("sending message")
            message = f"Low price alert! Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.arrival_city}-{flight.arrival_airport_code}, from {flight.departure_date} to {flight.arrival_data}."
            messanger.send_message(message)
