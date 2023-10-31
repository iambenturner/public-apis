import requests

response = requests.get('https://gnews.io/api/v4/top-headlines?category=business&lang=en&country=us&max=10&apikey=ec8e17b51a6dae7681010c90bef197d0')

print(response.status_code)
print(response.json())