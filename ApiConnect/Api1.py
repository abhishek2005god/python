# API Debugging Template

import requests

url = "https://dummyjson.com/products/1"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print(type(data))

print(data)