# class A:
#
#
#     def __init__(self, a):
#         self.a = 10
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self, value):
#         if value < 0:
#             raise Exception
#         self.__a = value
#
#     a = property(get_a, set_a)
#
# d = A(-10)
# d.a = 11

#
# print(d.a)

########################

# class Unit():
#
#     def __init__(self, health, armour):
#         self.__health = health
#         self.__armour = armour
#
#     def get_health(self):
#         return self.__health
#
#     def get_armour(self):
#         return self.__armour
#
#     def set_health(self, value):
#             if value < 50 and value > 0:
#                 self.__health = value
#
#     def set_armour(self, value):
#             if value > 90 and value < 100:
#                 self.__armour = value
#
#     health = property(get_health, set_health)
#     armour = property(get_armour, set_armour)#

# unit = Unit(50, 70)

# unit.health = 40
# unit.armour = 95
#
# print(unit.health)
# print(unit.armour)


# class A:
#
#     def some_method(self):
#         pass
#
#     @classmethod
#     def some_class_method(cls):
#         pass
#
#     @staticmethod
#     def some_static_method():
#         pass
#
#     @staticmethod
#     def some_static_method():
#         print('hello')
#
#
# a = A()
# a.some_static_method()

#
#
# a = iter([1, 2, 3, 4, 5])
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# class A:
#
#     def __init__(self, lim):
#         self.lim = lim
#         self.count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < self.lim:
#             self.count +=1
#             return self.count
#         else:
#             raise StopIteration
#
# a = A(6)
#
# for i in a:
#     print(i)




# def gen(n = 10):
#     for i in range(n):
#         yield i
#
# a = gen(3)
#
# for i in a:
#     print(i)

#__init__.py

# class A:
#
#     def __init__(self):
#
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         fib = self.a
#
#         if fib > self.limit:
#             raise StopIteration
#
#         self.a, self.b = self.b, self.a + self.b
#         return fib
#
#
#
# a = A(100)
#

## print(next(a))
## print(next(a))
## print(next(a))
## print(next(a))


# for i in a:
#     print(i)


#################################
#iterator - file in the same folder, A - class in file

# from iterator import A
#
# a = A(15)
#
# for i in a:
#     print(i)

################################
#iterator - file in the folder modules, I - class in file

# from modules.iterator import I
#
# a = I(8)
#
# for i in a:
#      print(i)


class A:

    __slots__ = ['health', 'weight']

a = A()

a.health = 100
a.weight = 20