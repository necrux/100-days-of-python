#!/usr/bin/env python3
import configparser
from datetime import datetime, date
from os import path
import requests

AUTH_FILE = f'{path.expanduser("~")}/.keys'
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SPREADSHEET = "https://api.sheety.co/ae9f9115d7ab84c2e6e48a31a7295db6/copyOfMyWorkouts100DaysOfCode/workouts"

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

config = configparser.RawConfigParser()
config.read(AUTH_FILE)

id = config["nutritionix"]["id"]
key = config["nutritionix"]["key"]

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 99.79,
    "height_cm": 165.1,
    "age": 37,
}

headers = {
    "x-app-id": id,
    "x-app-key": key,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
response.raise_for_status()
data = response.json()["exercises"]
for exercise in data:
    sheet_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=SPREADSHEET, json=sheet_params)
