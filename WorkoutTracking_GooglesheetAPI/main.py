import requests
import datetime as dt
from requests.auth import HTTPBasicAuth
import os

# Find your APP ID & APP KEY at following Url
# and set them as environment variables.
NUT_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUT_APP_ID = "XXXX"
NUT_APP_KEY = "YYYY"


GENDER = "female"
WEIGHT_KG = 65
HEIGHT_CM = 165
AGE = 46

# Find your Authentication at following Url
# and set them as environment variables
SHEETY_END_POINT = "https://api.sheety.co/3506dabdbe0877b5ca52ccd976848dce/myWorkouts/workouts"
SHEETY_USER_NAME = "AAAA"
SHEETY_PASSWORD = "BBBB"
SHEETY_BASIC_AUTHENTICATION = "CCCC"

# In case of adding the following Environment Variables
os.environ["NUT_APP_ID"] = NUT_APP_ID
os.environ["NUT_APP_KEY"] = NUT_APP_KEY
os.environ["SHEETY_END_POINT"] = SHEETY_END_POINT
os.environ["SHEETY_USER_NAME"] = SHEETY_USER_NAME
os.environ["SHEETY_PASSWORD"] = SHEETY_PASSWORD
os.environ["SHEETY_BASIC_AUTHENTICATION"] = SHEETY_BASIC_AUTHENTICATION

nut_app_id = os.environ.get("NUT_APP_ID")
nut_app_key = os.environ.get("NUT_APP_KEY")
sheety_end_point = os.environ.get("SHEETY_END_POINT")
sheety_user_name = os.environ.get("SHEETY_USER_NAME")
sheety_password = os.environ.get("SHEETY_PASSWORD")
sheety_basic_auth = os.environ.get("SHEETY_BASIC_AUTHENTICATION")

def get_exercise_result(exerciser_text):
    nut_params = {
        "query": exerciser_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    headers = {
        "x-app-id": nut_app_id,
        'x-app-key': nut_app_key,
    }

    # POST
    response = requests.post(url=NUT_END_POINT, json=nut_params, headers=headers)
    data = response.json()
    return data


## No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
# # Basic Authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         YOUR USERNAME,
#     YOUR PASSWORD,
#     )
# )
#
# # Bearer Token Authentication
# bearer_headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )


def post_data_to_google_sheet(data):
    basic = HTTPBasicAuth(username=sheety_user_name, password=sheety_password)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {sheety_basic_auth}",
    }

    d = dt.datetime.now().strftime("%d/%m/%Y")
    t = dt.datetime.now().strftime("%X")

    exercise_list = data["exercises"]

    for exercise in exercise_list:
        name = f"{exercise["name"].title()}" if exercise["name"] is not None else "_"
        duration_min = f"{exercise["duration_min"]}" if exercise["duration_min"] is not None else "0"
        nf_calories = f"{exercise["nf_calories"]}" if exercise["nf_calories"] is not None else "0"

        sheety_params = {
            "workout": {
                "date": f"{d}",
                "time": f"{t}",
                "exercise": f"{name}",
                "duration": f"{duration_min}",
                "calories": f"{nf_calories}",
            }
        }

        # POST
        response = requests.post(url=sheety_end_point, json=sheety_params, headers=headers, auth=basic)
        print(response.text)


def save_today_data_into_google_sheet():
    text = input("Tell me which exercise you've done: ")
    result = get_exercise_result(text)
    post_data_to_google_sheet(result)


# save_today_data_into_google_sheet()

# def subset_2d_array(arr, start_row, end_row, start_col, end_col):
#     return [row[start_col:end_col] for row in arr[start_row:end_row]]
#
# input_array = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# subset = subset_2d_array(input_array, 0, 2, 1, 3)
# print("Subset of the 2D array:")
# for row in subset:
#     print(row)


