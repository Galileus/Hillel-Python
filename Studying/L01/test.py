s = 'hello world'

list = [1, 5, 56, '23', [4, '5'], 5, 6, 6, 6, 88, 6909, 63645]
print(list,  'my list')
l = len(list)
print(l, ' - list length')
a = list[len(list)// 2 +1]
print(a, ' is the middle of the list ')

del list[-1]
print(list,  'my new list')

a = list.pop(3)
print(a,  '{var a - deleted from list}')

print(list,  '{my new list}')