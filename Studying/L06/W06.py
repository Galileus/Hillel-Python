# list = [1, 9, 10, 22]
#
# list = sorted( [str(i) for i in list] , reverse=True)
# print(''.join(list))

#
# lst = [2, 4, 3, 1, 5, 6, 8]
# #
# def binary(lst, x):
#
#     first = 0
#     last = len(lst) - 1
#     found = False
#
#
#
#     while first <= last:
#         mid = (first + last) // 2
#
#         if lst(mid) == x:
#             found = True
#         else:
#
#             if lst(mid) > x:
#                 first = mid + 1
#             else:
#                 last = mid -1
#
#
#     return found
#
#
# binary(lst, 5)
# #


# # f = open ('new', 'w')
# f = open ('new.txt', 'a')
#
# # print(f.read())
# f.write('ergwe\n')
#
# f.write('ergwe\n')
# f.close()


# with open ('new.txt', 'a') as f:
#     f.write('wwww\n')
#
# print('hello')

lst = []

with open ('new.txt', 'r') as f:
    for i in f.readlines():
        tmp = i[:-1].split(', ')
        lst.append(
            {
                'name': tmp[0],
                'weight': tmp[1]
            }
        )

print(lst)



