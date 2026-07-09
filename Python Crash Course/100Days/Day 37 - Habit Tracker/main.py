import os
from http.client import responses
from datetime import datetime
import requests
from api import ApiCall as aPI
from dotenv import load_dotenv

USER = "sdathompson"
TOKEN = "h3u4ity9hg39"
PIX_END = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# 1. Create a user-account on pixe.la
# response = aPI().api_post(end="https://pixe.la/v1/users", para=user_params)

# 2. Create a graph endpoint for posting
graph_endpoint = f"{PIX_END}/{USER}/graphs"

# Graph parameters
graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

# Needed for an extra level of security
headers = {
    "X-USER-TOKEN": TOKEN
}
# 3. Post the graph
# run_resp = aPI().api_post(end=graph_endpoint, para=graph_config, head=headers)

#4. Post a pixel
today_date = datetime.now()
pixel_endpoint = f"https://pixe.la/v1/users/{USER}/graphs/{graph_config["id"]}"

pixel_config = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": "3",
}

# Post pixel request for today's date
# run_pixel_resp = aPI().api_post(end=pixel_endpoint, para=pixel_config, head=headers)

update_endpoint = f"{pixel_endpoint}/{today_date.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# Put request - changes the value in today's date to the quantity in new_pixel_data
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

run_pixel_resp = aPI().api_delete(end=update_endpoint, head=headers)



