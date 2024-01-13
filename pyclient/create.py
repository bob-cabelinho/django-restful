import requests

endpoint = "http://localhost:8000/api/"

data = {
    "title": "garrafa",
    "price": 123.00,
    "description": "fdkaiusdoi"
}

response = requests.post(
    endpoint,
    json=data
) # HTTP POST REQUEST

print(response.json())
print(response.status_code)
