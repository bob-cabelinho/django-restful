import requests, json

endpoint = "http://localhost:8000/products/"

response = requests.get(endpoint)
print(json.loads(response.text))