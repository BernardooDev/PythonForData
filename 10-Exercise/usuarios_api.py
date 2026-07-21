import requests

url = "https://jsonplaceholder.typicode.com/users"

users = requests.get(url).json()

for user in users:
    print(f"Nome: {user['name']}")
    print(f"Email: {user['email']}")
    print()