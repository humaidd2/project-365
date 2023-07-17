import requests
import datetime


TOKEN = ""
USERNAME = "humaidd20"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"



today_date = str(datetime.date.today())
today_date = today_date.replace("-", "")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_params = {
    "id": "b613",
    "name": "Python Day 100",
    "unit": "commit",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
post_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

# pixel_params = {
#     "date": today_date,
#     "quantity": "2",
# }

# response = requests.post(url=post_a_pixel_endpoint, headers=headers, json=pixel_params)
# print(response.text)


# UPDATE A PIXEL

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today_date}"
# quantity = input("quantity to update: ")
# response = requests.put(update_endpoint, headers=headers, json={"quantity": quantity})
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{today_date}"
response = requests.delete(delete_endpoint, headers=headers)
print(response.text)

