# list = [1, 2, 3, 4, 5]
#
# def func (list):
#
#     if len(list) == 0:
#         return 0
#
#     return list[0] + sum(list[1:])
# print(func(list))


# def func ():
#     l = 1
#
#     def f2():
#         nonlocal l
#         l = l + 10
#     f2()
#     print(l)
#
# func()

# import time
#
# t1 = time.time()
# print(t1)
#
# def func ():
#     for i in range(1000000):
#         k = i ** 2
#
# t1 = time.time()
# func()
# t2 = time.time()
# print(t2 - t1)

# def func(f):
#     print('!!!')
#     f()
#
# def func2():
#     print('hello')
#
#
# func(func2)

# def counter(f):
#
#     def wrapper(n):
#         wrapper.c += 1
#         print('i`m running', wrapper.c)
#         res = f(n)
#         return f(n)
#     wrapper.c = 0
#     return wrapper
#
# @counter
# def func (n):
#     return n ** 2
#
# print(func(3))
# print(func(4))

# import time
# def counter(f):
#
#     def wrapper(n):
#         t1 = time.time()
#         res = f(n)
#         t2 = time.time()
#         print('im running', t2 - t1)
#         return res
#
#     return wrapper
#
# @counter
# def func (n):
#     return n ** 2
#
# print(func(3))
# print(func(4))


#################  zip

# a1 = ['a', 'b', 'c']
# a2 = ['d', 'e', 'f']
# a3 = [7, 8, 9]
#
# c = zip(a1, a2, a3)
# print(dict(c))


# list = [2, 3, 4]
# def func (list):
#
#     l = []
#     for i in list:
#         l.append(i**2)
#
#     return l
#
# print(func(list))


# def sq(n, k):
# # #     return n + k
# # #
# # # a = [2, 3, 4]
# # # b = [5, 3, 0]
# # #
# # # res = map(sq, a, b)
# # #
# # # print(list(res))




# def sq(n, k):
#     return n + k
#
#
# a = [2, 3, 4]
# b = [5, 3, 0]
#
# res = map(lambda x, y: x + y, a, b)
#
# print(list(res))

# func = lambda a, x: a + x
# print(func(3, 4))
#
# func = lambda x: x ** 2
# print(func(3))


# def sq(n):
#     return  n** 0.5
#
# a = [9, 25, 16]
#
# # res = map(sq, a)
# res = map(lambda n: n ** 0.5, a)
#
# print(list(res))

a = [-2, -3, 3, 2, 1]

# def func (a):
# #     l = []
# #     for i in a:
# #         if i > 0:
# #             l.append(i)
# #     return l
# #
# # print(func(a))


# def func (x):
#     return x > 0
#
# res = filter(func, a)
# print(list(res))


a = [1, 2, 3, 4, 5]

a = [i**2 for i in a]

# a = [i for i in range [1,1000]]

print(a)

