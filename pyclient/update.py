import requests


product_id = input("Product ID:>")
title = input("Title:>")
price = input("Price:>")
description = input("Descriptions:>")

endpoint = f"http://localhost:8000/api/products/{product_id}/update/"

data = {
    "title": title,
    "price": price,
    "description": description
}

response = requests.put(endpoint, json=data)

print(response.json())
print(response.status_code)