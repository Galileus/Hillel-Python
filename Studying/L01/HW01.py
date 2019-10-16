#1.Встановити python і pycharm - done

#2 Створити новий проект - done

#3 Знайти остачу від ділення 121 на 12, і скільки націло поділиться 134 на 7

print(121 % 12)#1
print(134 // 7)#19

#4 Обчислити 4 в степені 7

print(4 ** 7)#16384

#5 Зробити зріз другої половини довільного списку

list = [1, 5, 56, '23', [4, '5'], 5, 6, 6909, 63645]
print(list, 'my list')
lengh = (len(list))
mid = (len(list) // 2 + 1)
print(list[mid:])

#6 зробити зріз з 4го по 8й елемент списку

print(list[4:8], 'my new list 1')

#7 дістати зі списку остатній елемент і помножити його на 10

a = list[-1]
print(a * 10, 'result')

#8 видалити 3й елемент списка і вивести його на екран

a = list.pop(3)
print(a , '3й елемент')
print(list, 'my new list 2')


#9 добавити в середину списку новий елемент зі значенням 100
print(mid,  'the middle of the list')
list.insert(mid, 100)
print(list, 'my new list 3')

#10 * зробити копію списку
new_list = list[:]

print(list, 'my old list')
print(new_list, 'my new list')

new_list_1 = list.copy()
print(new_list_1, 'my new list_1')