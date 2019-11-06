#1. Зробити зі списка новий список елнментами якого будуть добуток
# всіх чисел масива крім поточного:
# [1,2,3,4] ---> [24, 12, 8, 6]
# [4, 5, 10] —-> [5*10, 4*10, 4*5] —> [50, 40, 20]

lst = [4, 5, 10]
c = 0
d = 1
l = []
for i in range(len(lst)):
    c = c + 1
    print(i, c, lst[i])

for i in range(len(lst)):
    if c !=
    d = d * lst[i]
    print(d)






#2 Перевірити чи є строка емейлом: ( необхідно перевірити чи є
# строка формату xxxxxx@xxx.xx, перша буква не є цифрою, не містить
# ніяких спецсимволів типу % і ?, а також має довжину першої частини
# більше ніж 3


#3 Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90
# зустрінеться в списку то перервати його роботу

# for i in range (100):
#     if i % 2 == 0:
#         if i == 90:
#             break
#         elif i == 6 or i == 8 or i == 86:
#             continue
#         else:
#             print(i)



#4 Скільки існує комбінацій пароля 4 символів, якщо відомо що
# друга цифра 4, 5 або 7, перша не 0, третя менша 6 а четверта більша 7







#5 . За допомогою filter залишити в списку тільки парні числа
#
# a = [-2, -3, 3, 2, 1]
#
# def fil(x):
# 	if x > 0 and x % 2 == 0:
# 		return x
#
# res = list(filter(fil,a))

# print(res)




#6 Є файл з даними учнів у форматі Прізвище;ім’я;зріст
# Написати функцію що зчитує дані з файлу, функцію що добавляє
# учня до списку, функцію що перевіряє чи є валідним формат
# даних що вводить користувач, три функції що обчислюють максимальний
# , мінімальний і середній зріст


# lst = []
# with open ('new.txt', 'r') as f:
#
#     for i in f.readlines():
#         tmp = i[:-1].split('; ')
#         lst.append(
#             {
#                 'Surname': tmp[0],
#                 'Name': tmp[1],
#                 'heigt': tmp[2]
#             }
#         )
#
# print(lst)

# #
# while True:
#     try:
#         a = input('enter your surname : ')
#         if a == None or a == '':
#             print('Invalid input surname. Please try again')
#             continue
#     except Exception as e:
#         print('Invalid input surname. Please try again')
#         continue
#
#     try:
#         b = input('enter your name : ')
#         if b == None or b == '':
#             print('Invalid input name. Please try again')
#             continue
#     except Exception as e:
#         print('Invalid input name. Please try again')
#         continue
#
#     try:
#         c = int(input('enter your height (cm) : '))
#     except Exception as e:
#         print('please enter a number, not less then 100')
#         continue
#
#     if c <= 100 or c > 250:
#         print('wrong heigt')
#         continue
#
#
#     with open('new.txt', 'a') as f:
#         c = str(c)
#         f.writelines(a + '; ' + b + '; ' + c  +'\n')
#
#         i = input('wanna finish ?(y/n) : ')
#
#         if i == 'y':
#             break
#         else:
#             continue
#
#
#
# lst = []
# nlst = []
# big = 0
# smal = 0
# mid = 0
# with open ('new.txt', 'r') as f:
#
#     for i in f.readlines():
#         tmp = i[:-1].split('; ')
#         lst.append(tmp)
#     print(lst, ' \n')
#
#     for i in range(len(lst)):
#
#         for j in range(1):
#             # print(lst[i][2])
#             mid += int(lst[i][2])
#
#             if int(lst[i][2]) > big:
#                 big = int(lst[i][2])
#
#             smal = int(lst[0][2])
#             if int(lst[i][2]) < smal:
#                 smal  = int(lst[i][2])
#
#     print(big, 'the tallest')
#     print(smal, 'the smalles')
#     print(mid/len(lst), 'mid heigt')

