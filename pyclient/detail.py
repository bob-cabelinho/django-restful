import requests

endpoint = 'http://localhost:8000/products/9/'

response = requests.get(endpoint)

print(response.json())
print(response.status_code)