#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from users_management import User_Management


users_m = User_Management()
tup = users_m.new_user()

flight_search = FlightSearch()
data_M = DataManager()
data_M.post_users(tup[0], tup[1], tup[2])
not_M = NotificationManager()

sheet_data = data_M.get_destination_data()

for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flight_search.get_destination_code(data['city'])
        response = data_M.update_destination_codes(id=data["id"], iata=data["iataCode"])

for row in sheet_data:
    flight_d = flight_search.flight_search_check(data=row)

    if flight_d is None:
        print(f" No flights found from London to {row['city']}")
        continue
    if row['lowestPrice'] > flight_d.price:
        users = data_M.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low Price alert.! Only $ {flight_d.price} to fly from {flight_d.origin_city}-{flight_d.origin_airport} to {row['city']}-{row['iataCode']}, from {flight_d.out_date} to {flight_d.return_date}",

        if flight_d.stop_overs > 0:
            message = f"{message}\nFlight has {flight_d.stop_overs} stop over, via {flight_d.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight_d.origin_airport}.{flight_d.destination_airport_code}.{flight_d.out_date}*{flight_d.destination_airport_code}.{flight_d.origin_airport}.{flight_d.return_date}"

        not_M.send_emails(msg1=message, to_email=emails, link=link)








