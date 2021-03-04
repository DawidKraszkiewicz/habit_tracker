import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "your pixe.la token"
USERNAME = "your pixe.la username"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes/no",
    "notMinor": "yes/no"
}
# here's how you create your account on pixela, change data in user_params for your own use
# https://docs.pixe.la/entry/post-user
# response = requests.post(url=pixela_endpoint, json=user_params) create a new
# graph: modify data for your own use
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "id of graph goes here",
    "name": "name of graph",
    "unit": "whatever unit you wish",
    "type": "int/float",
    "color": "momiji"
}
header = {
    "X-USER-TOKEN": TOKEN
}
# send a post request creating a new graph
requests.post(url=graph_endpoint, json=graph_config, headers=header)

# update a pixel
today = datetime.now()
print(today)
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "quantity of how much you did"
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)