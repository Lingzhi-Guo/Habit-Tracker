import requests
from datetime import datetime

endpoint = "https://pixe.la/v1/users"
token = "dab3b5hi239gfk45bdpo9"
user_name = "guolingzhi"
graph_id = "graph01"

# creating an account

parameters = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

create_account_requests.post(url=endpoint, json=parameters)
print(create_account_response.text)

# creating a graph

graph_endpoint = f"{endpoint}/{user_name}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}
graph_header = {
    "X-USER-TOKEN": token
}

create_graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_header)
print(create_graph_response.text)

# creating a pixel

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
quantity_to_record = input("How many pages did you read today?")
pixel_header = {
    "X-USER-TOKEN": token
}
pixel_config = {
    "date": formatted_date,
    "quantity": quantity_to_record,
}

pixel_endpoint = f"{endpoint}/{user_name}/graphs/{graph_id}"
create_pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=pixel_header)
print(create_pixel_response.text)

# edit a pixel

edit_pixel_date = 20240311
edit_pixel_endpoint = f"{endpoint}/{user_name}/graphs/{graph_id}/{edit_pixel_date}"
edit_pixel_parameters = {
    "quantity": "20"
}

edit_pixel_response = requests.put(url=edit_pixel_endpoint, json=edit_pixel_parameters, headers=pixel_header)
print(edit_pixel_response.text)

# delete a pixel
delete_pixel_date = 20240308
delete_pixel_endpoint = f"{endpoint}/{user_name}/graphs/{graph_id}/{delete_pixel_date}"
delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=pixel_header)
print(delete_pixel_response.text)
