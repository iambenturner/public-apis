import requests

response = requests.get('https://randomuser.me/api')

print(response.status_code)
print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)

nat = response.json()['results'][0]['nat']
print(nat)

first_name = response.json()['results'][0]['name']['first']
print(first_name)

