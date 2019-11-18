import requests
import time

class Request():

    def t1(self):
        self.t_1 = time.time()
        return self.t_1

    def get_ip(self):
        self.r = requests.get("https://ramziv.com/ip").text
        return self.r

    def dif(self):
        self.t_2 = time.time()
        return self.t_2 - self.t_1

    t1 = property(t1)
    t2 = property(dif)
    g = property(get_ip)

r = Request()

print(r.t1)
print(r.g)
print(r.t2)

