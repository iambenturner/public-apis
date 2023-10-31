import requests

response = requests.get('https://corporatebs-generator.sameerkumar.website/')

print(response.status_code)
print(response.json())
