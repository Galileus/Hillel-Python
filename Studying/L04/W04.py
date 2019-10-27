#
# from math import sin
#
# a = sin(10)
#
# print(a)

# def hellyea (n):
#     print('hellyea' * n)
#     return
#
# hellyea(4)

# def hellyea (n):
#
#     return n **2
#
# hellyea(4)

# def numb (a, b):
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     else:
#         print('fuck')
#
# print(numb(6, 4))

# def numb (a, b):
#     return a + b
#
# print(numb(6, 4))

list = [1, 23, 346, 345, 6, 36, 446, 3732, 4, 2, 2, 2, 99999]

# def max (list):
#     max = list[0]
#
#     for i in list:
#         if i > max:
#             max = i
#     return max
#
# print(max(list))

# def func (a, b):
#     return a + b
#
# print(func(3, 4))


# def func(a =  None):
#     if a is None:
#         a = []
#
#     a.append(1)
#     print(a)
#
# func()
# func()
# func([2, 3, 4])
# func([])
# func([3])
# func([])
# func()

# def func(*args):
#     return sum(args)
#
# print(func(1, 2, 3, 4))

#
# def func(**kwargs):
#     return kwargs
#
# print(func(b = 2, a = 4 ))

# def func(a, b *args, **kwargs):
#     return a**2 + b + sum()
#
# print(func(b = 2, a = 4 ))

# def func (a, b):#найбільший спільний дільник
#
#     while a != b:
#         if a > b:
#             a = a - b
#         if b > a:
#             b = b - a
#     return a
#
# print(func(16, 24))


#
# def func (n):
#     simple = True
#
#     for i in range (2, n):
#
#         if n % 1 == 0:
#             return False
#     return simple
#
#
# print(func(9))

# def func(a, b):
#     return a**2, b**2
#
# print(func(2, 3))
#

########№№№№№№№№№№№№№№№№№№№№№№№№№№33####виключення
# try:
#     a = 5 / 0
#
# except Exception as e:
#     print(e)
#
# print(a)

a = int(input('enter the number'))

try:
    while a != 5:
        a = int(input('enter the number'))

except Exception as e:
    print('enter the fucking number!!!')

else:
    print('what a hell??')
finally:
    print('what a fuck??')





