import requests

url = "https://dummyjson.com/quotes/random"

response = requests.get(url)

if response.status_code == 200:
    quote = response.json()

    print(quote["quote"])
    print(quote["author"])
    print(quote["id"])