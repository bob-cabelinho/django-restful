import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(
    endpoint,
    json={
        "title": "fones",
        "price": 123.33
    }
) # HTTP GET REQUEST

print(response.json())
print(response.status_code)
