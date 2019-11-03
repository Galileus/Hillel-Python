#1 за допомогою map перетворити числа в списку на їх дзеркальні (123 -> 321)

# l = [12, 34, 56]
#
# def rev(x):
#     return int(str(x)[::-1])
#
# res = list(map(rev, l))
#
# print(res)
#
# print (list(map(lambda x: int(str(x)[::-1]),l)))



#2 за дoпомогою filter залишити в списку слова довжина яких більше 5 букв

# l = ['fgsdfgdfgs', 'sdfg', '4', 'rsgwet']
#
# def filt(x):
#     if len(x) >= 5:
#         return x
#
# res = list(filter(filt, l))
# print(res)


# print (list(filter(lambda x: x if len(x) >= 5 else None, l)))


# 3 Написати декоратор що друкує в консоль аргументи з якими визивалася функція
#
# def log(func):
#
#     def wrapper(*args, **kwargs):
#         print('args log -', args)
#         print('kwargs log -', kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def add(a, b):
#     return a + b
#
# print(add(3, 45), 'res add')
#
# @log
# def add2(a, b, c):
#     return a + b + c
#
#
# print(add2(2, 10, 5), 'res add2')
#
#
#4 За допомогою рекурсії знайти суму перших 100 натуральних чисел
#
# def sum(x):
#     if x == 1:
#         return 1
#     return x + sum(x - 1)
#
# print(sum(100))

#5 Згенерувати список чисел від 0 до 200 що діляться на 7

# lst = [i for i in range(201) if i % 7 == 0 ]
# print(lst)

#
# def func(x):
#     list = []
#     for i in range(x+1):
#         if i % 7 == 0:
#             list.append(i)
#
#     print(list)
# func(200)


# l = []
# def gen(a, b):
#
#     if a < b+1:
#         if a % 7 == 0:
#             l.append(a)
#         gen(a+1,b)
#
# gen(0, 200)
# print(l)
