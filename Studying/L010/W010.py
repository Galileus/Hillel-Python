import requests

r = requests.request('GET',
                     'https://reqres.in/api/users?per_page=20'
                     )
res = r.json()

# print(r.status_code)
print(res)
print(res['data'])

for i in res['data']:
    print(i['email'])