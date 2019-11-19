import requests
import time

class Request():


    def __init__(self):
        self.__sourse = 'https://ramziv.com/ip'
        self.__t_1 = time.time()

    def get_url(self):
        return self.__sourse

    def set_url(self, url):
        self.__sourse = url

    def get_req(self):
        self.r = requests.get(self.__sourse)
        self.res = self.r.json()
        return (self.res['ip'])

    def get_time(self):
        self.__t_2 = time.time()
        return self.__t_2 - self.__t_1

    url = property(get_url, set_url)
    req = property(get_req)
    time = property(get_time)

r = Request()

r.url = 'https://ipinfo.io/'

print(r.req)
print(r.time)







