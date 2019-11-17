# class A:
#
#     def __init__(self):
#         self.__a = 10
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self,value):
#         self.__a = value
#
#     a = property(get_a, set_a)
#
# d = A()
# d.a = 12
# print(d.a)

# class Warrior():
#
#     def __init__(self):
#         self.__health = 50
#         self.__armour = 90
#
#     def get_health(self):
#         return self.__health
#
#     def get_armour(self):
#         return self.__armour
#
#     def set_health(self,value):
#         if value > 0 and value < 50:
#             self.__health = value
#
#     def set_armour(self,value):
#         if value > 90 and value <= 100:
#             self.__armour = value
#
#     health = property(get_health, set_health)
#     armour = property(get_armour, set_armour)
#
# warrior = Warrior()
#
# print(warrior.health)
# print(warrior.armour)
# warrior.health = 32
# warrior.armour = 56
# print(warrior.health)
# print(warrior.armour)
#
# print(warrior.__dict__)
#


# class A:
#     count = 0
#
#     def __init__(self):
#         self.counter()
#
#     @classmethod
#     def counter(cls):
#         cls.count += 1
#
# a = A()
# b = A()
# c = A()
#
# print(b.count)

# a = iter([1, 2, 3, 4, 5, 6])
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


# class A:
#
#     def __init__(self,lim):
#         self.lim = lim
#         self.a = 0
#         self.b = 1
#
#
#     def __iter__(self):
#         return self
#
#
#     def __next__(self):
#         fib = self.a
#
#         if fib > self.lim:
#             raise StopIteration
#
#         self.a, self.b = self.b, self.a + self.b
#
#         return fib
#
# a = A(100)
#
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