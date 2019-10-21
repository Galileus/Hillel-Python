# 1.a=”10”, b=”15”, a і b – це строки, обчислити b/a
# a = '10'
# a = int(a)
# b = '15'
# b = int(b)
# print(b / a)

# 2.створити словник в якому вказати основні дані про себе, словник має містить ключі значенням якого є інший словник, а також список
# friend_1 = {
#     "name": 'Tom',
#     "age": 26,
#     "sex": "Male"
# }
#
# friend_2 = {
#     "name": 'John',
#     "age": 25,
#     "sex": "Male"
# }
#
# friend_3 = {
#     "name": 'Max',
#     "age": 28,
#     "sex": "Male"
# }
#
# person = {
#     "name": 'Ihor',
#     "age": 28,
#     "sex": "Male",
#     "weight": 76,
#     "height": 176,
#     "maried": False,
#     'addres': {
#         "city": "Kyiv",
#         "street": "Obolonskyi.av",
#         "block": "20"
#     },
#     "status": "Student",
#     "friends": [friend_1, friend_2, friend_3]
# }
#
# print(person['friends'][1]['age'])
# print(person['age'])

# 3.створити масив з 10 елементів і перетворити його в tuple, вивісти зріз перших трьої елементів.
#

# list = [1, 3, 5, 7, 7, 45, 56, 76, 89, 90]
#
# tup = tuple(list)
# print(list)
# print(tup)
# print(tup[:3])

# 4.Є три числа, знайти найменше.

# a = int(input('enter a number -'))
# b = int(input('enter a number -'))
# c = int(input('enter a number -'))
#
# if a < b and a < c:
#     print('a')
# elif b < a and b < c:
#     print('b')
# elif c < a and c < b:
#     print('c')
# else:
#     print('not valid data')

#
# 5.Є три числа A, B, C – якщо вони впорядковані по зростанню то до кожного з них добавити 3 і вести їх нові значення,
# якщо ні то вивести їх протилежне число ( помножити на -1 ).



# a = int(input('enter a number -'))
# b = int(input('enter a number -'))
# c = int(input('enter a number -'))
#
# if a < b < c and a >= 0 and b >= 0 and c >= 0:
#
#     print(a+3, 'a')
#     print(b+3, 'b')
#     print(c+3, 'c')
#     a = int(input('enter a number -'))
#     b = int(input('enter a number -'))
#     c = int(input('enter a number -'))
# else:
#     print('fuck')
#     print(a*(-1), 'a')
#     print(b*(-1), 'b')
#     print(c*(-1), 'c')

# while True:
#     a = int(input('enter a number -'))
#     b = int(input('enter a number -'))
#     c = int(input('enter a number -'))
#
#     if a < b < c and a >= 0 and b >= 0 and c >= 0:
#
#         print('a is', a+3)
#         print('b is', b+3)
#         print('c is', c+3)
#         print('ok, lets change them!')
#         a = int(input('enter a number -'))
#         b = int(input('enter a number -'))
#         c = int(input('enter a number -'))
#         print('a is', a)
#         print('b is', b)
#         print('c is', c)
#         print('finished')
#         break
#     else:
#         print('fuck')
#         print(a*(-1), 'a')
#         print(b*(-1), 'b')
#         print(c*(-1), 'c')
#         print('try again')

#
# 6.Дано три числа. Знайти суму двох найбільших з них.
# a = 56
# b = 2
# c = 6
# res = 0
#
# if a > b or a > c:
#     res = res + a
# if b > c or b > a:
#     res = res + b
# if c > a or c > b:
#     res = res + c
#
# print(res, 'res')


# 7.Розв'язати квадратне рівняння ( пояснював на зайнятті )