
n = int(input('enter the number: '))
suma = 0

while n <= 2:
    n = int(input('enter the number: '))

for i in range(1,n):
        print(i)
        suma = suma + (1 / i)
        print(suma)
print('sum of numbers', suma)

