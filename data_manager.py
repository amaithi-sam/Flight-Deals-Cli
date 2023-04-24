
#This class is responsible for talking to the Google Sheet.
import requests

SHEETY_PRICES_ENDPOINT ="https://api.sheety.co//--------"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/---------"

class DataManager:

    def __init__(self):
       self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self, id, iata):


        new_data = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{id}", json=new_data)
        return response.json()

    def post_users(self, f_name, l_name, email):

        new_user = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email,
            }
        }
        response = requests.post(
            url=SHEETY_USERS_ENDPOINT, json=new_user
        )


    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data





