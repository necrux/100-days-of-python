#!/usr/bin/env python3
import configparser
from os import path, environ
import requests

CONFIG_FILE = f'{path.expanduser("~")}/.keys'

config = configparser.RawConfigParser()
config.read(CONFIG_FILE)
api_key = config["openweather"]["key"]
lat = environ.get('LAT')
lon = environ.get('LONG')

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
data = response.json()
weather_id = data["weather"][0]["id"]

if weather_id < 700:
    print("It's going to rain.")
