class Animal(object):

    def __init__(self, name, weight, height):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return self.name

a1 = Animal(name='Roma', height=100, weight=200)
#
print(a1)
#
# class Human(object):
#
#     def __init__(self, name, sex, height):
#         self.name = name
#         self.sex = sex
#         self.height = height
#
#
#
#     def __str__(self):
#         return self.name
#
# a1 = Animal(name='Roma', height=100, weight=200)
#
# h1 = Human(name='Vasia', sex='Male', height=175)
#
# print(a1.name)
# print(h1.height)
#
#
# class Dog(Animal):
#
#     def __init__(self, breed):
#         self.breed = breed
#
#     def barking(self, time):
#         print('gav gav' * time)
#
# # dog = Dog(name='Barsik', weight=245, height=345)
#
# # dog.barking(3)
#
# dog = Dog(breed='goood')
#
# print(dog.breed)
#
#
# class Stack(object):
#
#     def __init__(self):
#         self.items = []
#
#     def get(self):
#         if self.is_empty():
#             return None
#         return self.items.pop(-1)
#
#     def add(self, value):
#         self.items.append(value)
#
#     def is_empty(self):
#         if len(self.items) == 0:
#             return None
#
#     def count(self):
#         if len(self.items) == 0:
#             return None#
#
# stack = Stack()
# stack.add('a')
# stack.add('b')
# print(stack.items)
# print(stack.get())
# print(stack.get())



# class Animal(object):
#     __legs = 4
#
#     def def_legs(self):
#         print(self.__legs)
#
# animal = Animal()
#
# print(animal._Animal__legs)



#
# class People(object):
#
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         self.age = value
#
#         if value < 120:
#             self.__age = value
#
#
# person = People(100)
# print(person.get_age())

#
# class SuperMarket(object):
#
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#
#     def sq(self):
#         return self.lenght * self.width
#
#     def is_valid(self):
#         if self.sq() > 100:
#             return True
#
#         return False
#
# class Shop(SuperMarket):
#
#     def is_valid(self):
#
#
# market = Market()
#
# print(market.sq(2, 4))