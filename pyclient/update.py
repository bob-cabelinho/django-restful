import requests

endpoint = 'http://localhost/8000/products/9/update/'

data = {
    "title": "test_update",
    "price": 123123.09
}

response = requests.get(endpoint, json=data)

print(response.json())
print(response.status_code)