import requests
import time
seconds1 = time.time()
print("Seconds since epoch =", seconds1)



response = requests.request('GET', 'https://httpbin.org/get')

print(response.status_code)

seconds2 = time.time()
print("Seconds since epoch =", seconds2)

print(seconds1 - seconds2)
