#1. Знайти максимальне число в списку

list = [1, 23, 346, 345, 6, 36, 446, 3732, 4, 2, 2, 2]

# max = 0
# for i in list:
#     if i > max:
#         max = i

# print(max, 'max number')

#2. Знайти суму всіх чисел в списку що діляться на 3

# sum = 0
# for i in list:
#     if i % 3 == 0:
#         sum = i + sum
#         print(i)

# print(sum, 'sum all i')

#3. Вивести квадрати чисел від 10 до 30

# for i in range(10, 30):
#     print(i ** 2)

#4. вивести середнє значення в списку

# for i in list:
#     sum = i + sum
#
# mid = sum / len(list)
# print(mid, "mid")

#5. число n>2 вводиться з клавіатури, порахувати 1 + 1/2 + 1/3 + ... + 1/n

n = int(input('enter the number: '))
suma = 0

while n <= 2:
    n = int(input('enter the number: '))

for i in range(1,n):
        print(i)
        suma = suma + (1 / i)
        print(suma)
print('sum of numbers', suma)
