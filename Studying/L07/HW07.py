#Реалізувати класс Дек ( це те ж саме що черга і стер одночасно )
# , в ньому визначити методи: перевірки на те чи порожній дек,
# очистити дек, взяти елемент як з черги, взяти елемент як з стеку,
# заповнити дек рандомними числами - кількість чисел передається параметром.

import random
class Deck(object):

    def __init__(self):
        self.item = []

    def is_empty(self):
        if len(self.item) == 0:
            return self.item == []

    def addFront(self, value):
        self.item.insert(0, value)

    def addEnd(self, value):
        self.item.append(value)

    def getFront(self,value=0):
        if len(self.item) == 0:
            return None
        return self.item.pop(value)

    def getEnd(self):
        if len(self.item) == 0:
            return None
        return self.item.pop(-1)

    def clear(self,command):
        if command == 'clearall':
            self.item.clear()
        else:
            return None

    def pushRand(self,value):
        while len(self.item) != value:
            self.item.append(random.randrange(0, 999))


deck = Deck()

# deck.addFront(3)
# deck.addEnd(44)
# deck.addFront('1')
# deck.addEnd(4234)
# deck.addFront(78)
# # deck.clear('clearall')
#
# print(deck.item)
#
#
# print(deck.getEnd())
# print(deck.getFront())
# print(deck.getEnd())
# print(deck.getFront())

deck.pushRand(10)
print(deck.item)

print(deck.getFront())
print(deck.getFront())
print(deck.getFront())

print(deck.getEnd())
print(deck.getEnd())
print(deck.getEnd())

