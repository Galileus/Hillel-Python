#1.Функція що перевіряє чи є число більше 0

# print('lets try to check is a > 0 ?')
# try:
#     a = int(input('enter the value for a: '))
#
# except Exception as e:
#     print('enter the fucking number!!!')
#     a = int(input('enter the value for a: '))
#
# def func(a):
#     if a > 0:
#         print('a > 0, a = ', a)
#         return a
#     elif a == 0:
#         print('a = 0')
#         return a
#     else:
#         print('a < 0, a = ', a)
#         return a
# func(a)

#2 Функція що знаходить факторіал числа

# n = int(input('enter the value for n!: '))
#
# def fact (n, d=1):
#     for i in range (1, n+1):
#         d *= i
#
#     print(d)
# fact(n)

#3 Функцію що перевіряє чи є строка панаграмою

# a = input('enter your text (en):')
#
# def func (a):
#
#     l = []
#     for i in a:
#         l.append(i)
#
#     voc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
#      'x', 'y', 'z']
#     result = list(set(voc) - set(l))
#
#     if len(result) > 0:
#         print('your text isn`t panagram')
#     elif len(result) == 0:
#         print('your text isn`t panagram')
#     else:
#         print('what the f*** did you write??')
#
# func(a)

#4 функція що ділить два числа, обробити випадок ділення на 0
while True:
    try:
        a = int(input('enter the number for a: '))
        b = int(input('enter the number for b: '))

    except Exception as e:
        print('please enter a number')
        continue

    try:
        if a or b > 0:
            print(a / b)
            break

    except Exception as e:
        print('don`t use 0 or string for b !!!')
