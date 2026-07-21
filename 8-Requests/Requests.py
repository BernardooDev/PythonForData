import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)


dados = response.json()

#print(dados)

print(dados[0]["name"])
print(dados[0]["email"])