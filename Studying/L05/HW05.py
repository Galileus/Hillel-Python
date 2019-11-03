# #1 за допомогою map перетворити числа в списку на їх дзеркальні (123 -> 321)
#
list = [12, 34, 56]
#
#
# def rever(x):
#
#     return int(str(x)[::-1])
#
#
# print(rever(455))

print(list(map(lambda x: int(str(x)[::-1]), [1223, 345] )))


# функція що вертає більше менше довжин списка
#
# #3
#
# def log(func):
#
#     def wrapper(*args, **kwargs):
#         print('log-', args, ' ', kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper()#*argsm **kwargs
# @log
# def add(a, b):
#     return a + b
# @log
# def add2(a, b, c):
#     return a + b + c
#
# print(add(2, 10))
#
#
#
#
# lst = [i for i in range(201) if i % 7 == 0 ]