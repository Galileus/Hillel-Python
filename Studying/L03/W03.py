# # for i in range(0, 10, 2):#(from, to, step)
# #     print('hello')
#
# #
# #
# # a = [1, 2, 3, 4, 6, 5, 7, 8]
# #
# # for i in a:
# #     print(a[i] ,'--',  i)
# #
# # for i, j in enumerate(a):
# #     print(j , '--', i)
#
# # i = 0
# # while i < 10:
# #     print('hello ')
# #     i +=1 #i+i+1 _ i*=2 - i = i +2
#
# a = [1, 2, 3, 4, 6, 5, 7, 8]
#
# # for i in a:
# #     if i % 2 == 0:
# #         print(i)
#
#
# i = 0
# count = 0
# suma = 0
# while i < len(a):
#     i = i + 1
#
#     if i % 2 == 0:
#         count += 1
#         suma = suma + i
#         print(i)
#
#
# print(count, 'count')
# print(suma, 'suma')

# for i in range(10):
#     for j in range(10):
#         print(i, '--', j)

#1 - pair, #2 > 6 #3  8, 9   #4 unpair

# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#             for j in range(10):
#                 if j > 6:
#                     print(j)
#                         for k in range(10):
#                             if k == 8 or k == 9:
#                                 print(k)
#                                     for l in range(10):
#                                         if l % 2 == 1:
#                                             print(i, j, k, l)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i*j, end=' ')
#
# for i in range(10):
#     if i == 5:
#         continue

# a = 284655
# passw = int(input('enter a pass -'))
#
# while passw != a:
#     passw = int(input('enter a pass -'))
#
# print('successful!')

# a = 'femgow a jrlwqfgio the  owrhqtow in oweiqhr'
# print(a)
# a = a.split(' ')
# delt = ['a', 'the', 'in', 'the' ]
#
# for i in a:
#     if i in delt:
#         a.remove(i)
#
# s = ''.join(a)
# print(s)

# a = [0, 1]
#
# # for i in range (2,50):
# #     a.append(a[i - 1]+ a [i - 2])
# # print(a)
# i=2
# while i != 50:
#     a.append(a[i - 1]+ a [i - 2])
# print(a)