import requests

product_id = input("Product ID:>")

endpoint = f"http://localhost:8000/api/products/{product_id}/"

response = requests.get(endpoint)

print(response.json())
print(response.status_code)