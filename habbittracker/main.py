import requests
import datetime as dt

USERNAME = "palhimalaya"
TOKEN = "fgeyu4gf76ds3fgeuyfgefhgh"
ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PUT_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": ID,
    "name": "Coding_Tracker",
    "unit": "Hr",
    "type": "float",
    "color": "momiji",

}
# now = dt.datetime(year=2021, month=5, day=31)
now = dt.datetime.now()
today_date = now.strftime("%Y%m%d")

pixel_params = {
    "date": f"{today_date}",
    "quantity": input("How many hour did you code today."),
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

response = requests.post(url=PUT_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(response.text)

PIXEL_UPDATE_ENDPOINT = f"{PUT_PIXEL_ENDPOINT}/{today_date}"
update_data = {
    "quantity": "7"
}
# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_data, headers=headers)
# print(response.text)

# response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=headers)
# print(response.text)
