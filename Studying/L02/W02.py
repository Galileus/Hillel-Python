tup = (1, 2, 4, 5, 7)
print(tup[1:])

children_1 = {
    "name": 'Max',
    "age": 2,
    "sex": 'Male',
}

children_2 = {
    "name": 'Tom',
    "age": 12,
    "sex": 'Male',
}

person = {
    "name": 'Ihor',
    "age": 28,
    "sex": 'Male',
    "weigth": 76,
    "heigt": 175,
    "maried ":  False,
    "adress": {
        'city': 'Kyiv',
        'street': 'Lenina',
        'block': 25
    },
    "children": [children_1, children_2]
}

print(person['children'][1]['name'], 'is children_2 name')

print(person.keys())
print(person.values())
# #
# #
# # visa = {
# #     "name": 'Tom',
# #     "number": 1234523452345234
# # }
# #
# # cash = {
# #     "qt": 'UA',
# #     "val": 123423453
# #
# # }
# #
# # USA = {
# #     "name": 'USA',
# #     "val": '342ETYE5Y58'
# # }
# #
# # UA = {
# #     "name": 'UA',
# #     "val": 34258
# # }
# #
# # Canada = {
# #     "name": 'Canada',
# #     "val": 34254564568
# # }
# #
# # company = {
# #     "name":'MPT',
# #     "employee": 23,
# #     "direction":'SW',
# #     "payment": {
# #         'card': 'viza',
# #         'cash': 'UAH'
# #     },
# #     'parteners': [USA, UA, Canada]
# #
# # }
# #
# # print(company.keys())
# # print(company.values())
# #
# #
# # print(company['parteners'][0]['val'])
# # print(company['parteners'][2]['val'])
#
#
# # s = 'hello'
# # print(set(s))
#
#
#
# a = 6
# b = 2
# c = 32
#
# if a > b and a > c:
#     print('a the biggest')
# elif b > a and b > c:
#     print('b the biggest')
# else:
#     print('c the biggest')
#
#
# a = 1
# b = 4
#
# if a > 0 and b > 0 and a > b or a < b:
#     s = a * b
#     print(s, 'sq')
# else:
#     s = a ** 2
#     print(s, 'kv')
#
# a = None
#
# if a is None:
#     print('Hello')
#
# a = [1, 2, 3]
# b = a
# b[0] = 100
#
# if a is b:
#     print('a is b')
# else:
#     print('bla')


# a = 1000
# b = 1000
#
# if a is b:
#     print('True')
# else:
#     print('False')

# print(children_1.get('weight', 100))

# x = 10
#
# if 0 < x < 12:
#     print('hell yea')

# import math #or use from math import sqrt as sq(renamed func sqrt)
# a = 100
# print(math.sqrt(a))
#
# print(math.sin(a))

# a = [1, 3, 5, 8, 6]
#
# if 5 in a:
#     print('5 in a')

a = 'abcba'
if a == a[::-1]:
    print('true')

