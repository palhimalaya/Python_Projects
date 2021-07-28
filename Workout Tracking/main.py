import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 170.688
AGE = 20
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
print(username)

params = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}
auth = (
    username,
    password
)

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/d656b96683b8cf1e95091a477bf30123/myWorkouts/workouts"

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
result = response.json()

# .....................Start of Step 4 Solution..................#

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, auth=auth)
