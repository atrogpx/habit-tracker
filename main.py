import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "atro"
TOKEN = "hjgcfycte547"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
DATE = today.strftime("%Y%m%d")

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_pixel_params = {
    "date": DATE,
    "quantity": input("How many kilometers did you cycle today?")
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.json())

# put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
# put_pixel_params = {
#     "quantity": "8"
# }
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
