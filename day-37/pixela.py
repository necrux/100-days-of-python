#!/usr/bin/env python3
import configparser
from datetime import datetime
from os import path
import requests

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
AUTH_FILE = f'{path.expanduser("~")}/.keys'

CONFIG = configparser.RawConfigParser()
CONFIG.read(AUTH_FILE)
USERNAME = CONFIG["pixela"]["username"]
TOKEN = CONFIG["pixela"]["token"]
GRAPH_ID = "graph1"

PIXELA_GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs"
PIXELA_PIXEL_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# Create Pixela User
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
#print(response.text)

# Create Pixela Graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Exercise Graph",
    "unit": "Time",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_config, headers=headers)
#print(response.text)

# Create Pixela Graph Pixel
today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

#response = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
#print(response.text)