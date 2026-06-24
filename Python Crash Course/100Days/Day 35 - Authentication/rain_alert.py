import requests
import os

TO_LAT = 43.653225
TO_LON = -79.383186
OWM_END = "https://api.openweathermap.org/data/2.5/forecast"
# To export an environment variable, go to terminal and type: $env:{variableName}={variableContent}
# This will add a variable to the
api_key = os.environ.get("api_key")
# Current Weather Data Endpoint by City = https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

params_to = {
    "q": "Toronto",
    "appid": api_key,
}

params_to_5day = {
    "lat": TO_LAT,
    "lon": TO_LON,
    "appid": api_key,
}

curr_to_resp = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params_to)
curr_to_resp.raise_for_status()

to_5day_resp = requests.get(url=OWM_END, params=params_to_5day)
to_5day_resp.raise_for_status()
to_5day_data = to_5day_resp.json()
print(to_5day_data["list"][0]["weather"][0]["id"])

# if id < 700 : bring an umbrella
for w_id in to_5day_data["list"][:6]:
    if w_id["weather"][0]["id"] < 700:
        # Send an e-mail saying to bring an umbrella
        print ("Bring an umbrella!")
    else:
        print ("You don't need an umbrella")
