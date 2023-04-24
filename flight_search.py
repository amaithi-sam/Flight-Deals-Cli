import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "--------"

header = {
    "apikey": TEQUILA_API_KEY
}

today = datetime.today()
day_6_month = today + timedelta(days=6 * 30)
f_today = today.strftime("%d/%m/%Y")
f_6day = day_6_month.strftime("%d/%m/%Y")


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def get_destination_code(self, city_name: str) -> str:

        t_js = {
            "term": f"{city_name}",
            "location_types": "city",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query", params=t_js, headers=header)

        f_response = response.json()["locations"]
        code = f_response[0]['code']
        return code

    def flight_search_check(self, data, stop_overs=0):
        param = {
            "fly_from": "LON",
            "date_from": str(f_today),
            "date_to": str(f_6day),
            "curr": "USD",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": stop_overs,
            "fly_to": str(data['iataCode'])

        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                params=param,
                                headers=header
                                )
        try:
            data = response.json()["data"][0]

        except IndexError:
            # print(f"No flights found for {data['route'][0]['cityTo']} with direct flights")

            param["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                    params=param,
                                    headers=header
                                    )

            try:
                data = response.json()['data'][0]
            except:
                return None
            else:
                flight_search_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport_code=data["route"][0]["flyTo"],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]['local_departure'].split('T')[0])

                return flight_search_data

        else:
            flight_search_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport_code=data["route"][0]["flyTo"],
                stop_overs=0,
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]['local_departure'].split('T')[0])

            return flight_search_data
