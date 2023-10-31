import requests

response = requests.get('https://api.dicebear.com/7.x/open-peeps/svg')

print(response.status_code)
print(response.json())
