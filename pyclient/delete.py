import requests

product_id = input("Product ID:>")

endpoint = f"http://localhost:8000/products/{product_id}/delete/"

response = requests.delete(endpoint)
print(response.json)