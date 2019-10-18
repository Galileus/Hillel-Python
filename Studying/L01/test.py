s = 'hello world'

list = [1, 5, 56, '23', [4, '5'], 5, 6, 6, 6, 88, '6909', '63645']
print(list,  'my list')
l = len(list)
print(l, ' - list length')
a = list[len(list)// 2 +1]
print(a, ' is the middle of the list ')

del list[-1]
print(list,  'my new list')

b = list.pop(3)#using pop
print(b,  '{var a - deleted from list}')
print(list,  '{my new list [pop]}')

list.append(123)
print(list,  '{my new list [append 123]}')

list.insert(3, 456)
print(list,  '{my new list [insert 456]}')

c = list.copy()
print(c,  '{my  list copy}')


print(list[2:],  '{my new list [2:]}')
print(list[:2],  '{my new list [:2]}')
print(list[1::2],  '{my new list [1::2]}')

result = list[a:]
print(result, 'result')

result = list[4:8]
print(result, 'result [4:8]')

last = list.pop(-1)
print(last*10, 'last el * 10')
print(list, 'list')

third = list.pop(3)
print(third, 'third element')

list.insert(a, 100)
print(list, 'new list')

new_list = list.copy()
print(new_list, 'my new list')



z = 100

print(z, 'z')
print((z % 5) == 0)

print(type(list[-1]))
print(list)

print(list[::-1], 'unpair')

list.remove(100)
print(list, '3')

print('')

temp = []
print(list, 'my list')
print(new_list, 'my new list')
print(temp, 'my temp list')

word = input ("Введіть слово: ")
print('You have printed', word)
