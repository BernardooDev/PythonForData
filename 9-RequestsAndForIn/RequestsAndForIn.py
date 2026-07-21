import requests

url = "https://jsonplaceholder.typicode.com/users"

usuarios = requests.get(url).json()

for usuario in usuarios:
    print(
        usuario["name"],
        "-",
        usuario["email"]
    )