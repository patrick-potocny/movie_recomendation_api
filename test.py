import requests

BASE_URL = 'http://127.0.0.1:5000/'
movie = 'Batman'
response = requests.get(BASE_URL + f'api/{movie}')
    
print(response.json())
rec_movies = response.json()[movie].split('; ')
print('Recomended movies:')
for movie in rec_movies:
    print(20 * '-')
    print(f'{movie}')