#1. Зробити зі списка новий список елнментами якого будуть добуток всіх чисел масива крім поточного:
# [1,2,3,4] ---> [24, 12, 8, 6]
# [4, 5, 10] —-> [5*10, 4*10, 4*5] —> [50, 40, 20]

# l = [1, 2, 3, 4]
# #
# # # a = [1, 2, 3, 4, 6, 5, 7, 8]
# #
# for i in range(len(l)):
#
#     print(l[i],'--',i)



# def func (l):
#
#     if len(l) == 0:
#          return 0
#
#     return l[0] + sum(l[1:])
#
# print(func(l))

# list = [1, 9, 10, 22]
#
# list = sorted( [str(i) for i in list] , reverse=True)
# print(''.join(list))


#
# l = [1, 2, 3, 4]
#
# list = l[1:]
#
# list =
# print(list)



# res = 1
# for i in range(len(l)):
# 	res = l[i+1] * res
# print(res)




# a = [a[i]*a[i-1] for i in range (len(a-1))]

# a = [i for i in range [1,1000]]

# a = [i*2 for i in a]
#
# print(a)


# for i in range(len(l)):
#     print(i)




l = [1, 2, 3, 4, 5]
res = 1
for i in range(len(l)+1):

	if i != 0:
		res = i * res
		print(res)


