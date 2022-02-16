import requests
from datetime import datetime
import os

APP_ID = "71b525a1"
APP_KEY = "de17ae0e8967ca2a2e6bb24218ae53a9"
GENDER = "male"
WEIGHT = 82
HEIGHT = 182
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise_params = {
    "query": input("What exercise did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers).json()

sheety_endpoint = "https://api.sheety.co/432244d856c8d37724f83cfc61d599be/workoutTracking/workouts"
today = datetime.now()
sheety_bearer = "sheetyworkouttrack"
headers2 = {
    "Authorization": f"Bearer {sheety_bearer}"
}

for exercise in response["exercises"]:
    body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    result = requests.post(url=sheety_endpoint, json=body, headers=headers2)
    print(result.text)

# res = requests.get(url=sheety_endpoint, headers=headers2)
# print(res.text)
