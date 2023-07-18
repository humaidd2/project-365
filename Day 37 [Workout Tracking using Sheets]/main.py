import requests
import datetime
from dotenv import load_dotenv
import os

GENDER = "male"
WEIGHT = 74
AGE = 21
APPID = os.getenv("APPID")
APPKEY = os.getenv("APPKEY")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
sheety_login = (USERNAME, PASSWORD)

headers = {
    "x-app-id": APPID,
    "x-app-key": APPKEY,

}
exercise_input = input("What exercise did you perform: ")
exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "age": AGE
}
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_response = requests.post(url=exercise_url, headers=headers, json=exercise_params).json()
print(exercise_response)

current_date = str(datetime.date.today()).replace("-", "/")
for exercise in exercise_response['exercises']:
    time = exercise['duration_min']
    exercise_name = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

sheetyurl = "https://api.sheety.co/fefd8184903fff1c378dd57c29d88879/myWorkout/sheet1"
sheetjson = {
    "sheet1": {
        "date": current_date,
        "time": time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories
    }

}
sheetresponse = requests.post(url=sheetyurl, json=sheetjson, auth=sheety_login)
print(sheetresponse.json())
