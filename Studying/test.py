#1 за допомогою map перетворити числа в списку на їх дзеркальні (123 -> 321)

# list = [12, 34, 56]



# def sq(n, k):
#     return n + k
#
# a = [2, 3, 4]
# b = [5, 3, 0]
#
# res = map(sq, a, b)
#
# print(list(res))

#
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


list = [1, 2, 3, 4, 5, 6, 7, 8]

def func(list):
    if not list:
        return 0

    return list[0] + func(list[1:])

print(func(list))