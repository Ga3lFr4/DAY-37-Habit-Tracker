import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "meditation"
HEADER = {
    "X-USER-TOKEN": TOKEN,
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# request = requests.post(url="https://pixe.la/v1/users", json=user_params)
# request.raise_for_status()

graph_params = {
    "id": "meditation",
    "name": "Meditation",
    "unit": "minutes",
    "type": "int",
    "color": "ichou",
    "timezone": "CET",
}

# graph = requests.post(headers=headers, url=f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_params)
# print(graph.text)

graph_url = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}.html"
# print(graph_url)

now = datetime.now()
today = now.strftime("%Y%m%d")

add_pixel_params = {
    "date": today,
    "quantity": "0",
}

modify_pixel_data = {
    "quantity": "15",
}

# add_pixel = requests.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", headers=HEADER, json=add_pixel_params)
# print(add_pixel.text)

# modify_pixel = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=HEADER, json=modify_pixel_data)
# print(modify_pixel.text)

delete_pixel = requests.delete(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=HEADER)
print(delete_pixel.text)

