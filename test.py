import requests

BASE_URL = 'http://127.0.0.1:5000/'

response = requests.get(BASE_URL + 'api')

print('API:')      
print(response.json())
