import requests, json
from getpass import getpass

endpoint = "http://localhost:8000/api/products/"
endpoint_auth = "http://localhost:8000/api/auth/"

data_auth = {
    "username": "cabelinho",
    "password": getpass()
}

auth_response = requests.post(endpoint_auth, json=data_auth)

if auth_response.status_code == 200:
    headers = {
        "Token": f"Token {auth_response.json()['token']}"
    }
    respose = requests.get(endpoint, headers=headers)
    print(json.loads(respose.text))