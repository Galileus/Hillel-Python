import requests

r = requests.request('GET',
                     'https://reqres.in/api/users?per_page=20'
                     )
response = r.json()

print(response['data']['email'])