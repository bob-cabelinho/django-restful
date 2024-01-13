import requests

endpoint = "http://localhost:8000/api/"

title = input("Title:>")
price = input("Price:>")
description = input("Descriptions:>")
if description is not None:
    description = title+"__product"

data = {
    "title": title,
    "price": price,
    "description": description
}

response = requests.post(
    endpoint,
    json=data
) # HTTP POST REQUEST

print(response.json())
print(response.status_code)
