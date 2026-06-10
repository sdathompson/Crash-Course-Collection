from http.client import responses

import requests

# GE Runescape API = https://secure.runescape.com/m=itemdb_rs/api/info.json
# To get the Old School API replace "m=itemdb_rs" with "m=itemdb_oldschool"



# Get a full list of all item IDs
GEID_response = requests.get(url="https://oldschool.runescape.wiki/?title=Module:GEIDs/data.json&action=raw&ctype=application%2Fjson")
GEID_response.raise_for_status()
GEID_data = GEID_response.json()

search_input = input("What item do you want to get pricing for?: ")
if search_input is not None:
    search_id = GEID_data[search_input]

GEdetails_response = requests.get(url=f"https://secure.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item={search_id}")
GEdetails_response.raise_for_status()
GEdetails_data = GEdetails_response.json()

print(GEdetails_data)


