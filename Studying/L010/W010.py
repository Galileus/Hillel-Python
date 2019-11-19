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
        return (self.r.content)

        # return (self.r.json())

    url = property(get_url, set_url)
    req = property(get_req)




r = Request()

r.url = 'https://2ip.ua/ru/'

print(r.req)






