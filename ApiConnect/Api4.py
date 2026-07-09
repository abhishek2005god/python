import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke = response.json()

    print(joke["setup"])
    print(joke["punchline"])
    print(joke["id"])
    print(joke["type"])
    print(joke["status"])