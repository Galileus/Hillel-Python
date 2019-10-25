list = [1, 23, 346, 345, 6, 36, 446, 3732, 4, 2, 2, 2, 99999]

#1. Знайти максимальне число в списку

# max = 0
# for i in list:
#     if i > max:
#         max = i
# print(max, 'max number')

#########################################

# i = 0
# max = 0
# while i < len(list):
#     if list[i] > max:
#         max = list[i]#
#     i = i + 1
#
# print(max, 'max number')

#2. Знайти суму всіх чисел в списку що діляться на 3

# sum = 0
# for i in list:
#     if i % 3 == 0:
#         sum = i + sum
#         print(i)
# print(sum, 'sum all i')

#################################################

# i = 0
# sum = 0
# while i < len(list):
#     if list[i] % 3 == 0:
#         sum = list[i] + sum
#     i = i + 1
# print(sum, 'sum all i')

#3. Вивести квадрати чисел від 10 до 30

# for i in range(10, 30):
#     print(i ** 2)

##############################################
# i = 10
# while i <= 30:
#     print(i ** 2)
#     i = i + 1

#4. вивести середнє значення в списку

# sum = 0
# for i in list:
#     sum = i + sum
#
# mid = sum / len(list)
# print(mid, "mid")

################################################

# i = 0
# sum = 0
#
# while i < len(list):
#     sum = list[i] + sum
#     i = i + 1
#
# mid = sum / len(list)
# print(mid, "mid")

#5. число n>2 вводиться з клавіатури, порахувати 1 + 1/2 + 1/3 + ... + 1/n

# n = int(input('enter the number: '))
# sum = 0
#
# while n <= 2:
#     n = int(input('enter the number: '))
#
# for i in range(1,n):
#         print(i)
#         sum = sum + (1 / i)
#         print(sum)
# print('sum of numbers', sum)

##################################################

# n = int(input('enter the number: '))
# sum = 0
# i = 1
#
# while n <= 2:
#     n = int(input('enter the number: '))
#
# while i < n :
#     print(i)
#
#     sum = sum + (1 / i)
#     print(sum)
#     i = i + 1
# print('sum of numbers', sum)




