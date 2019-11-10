# class Animal(object):
#
#     def __init__(self ,height, weight, name):
#         self.height = height
#         self.weight = weight
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# a1 = Animal(height = 155, weight = 320, name = 'Ihor')
#
# print(a1)


class Human(object):

    def __init__(self, name, age, height):
        self.name = 'Name'
        self.age = "age"
        self.height = 'height'

        self.sex = 'man'

class Student(Human):

    def __init__(self, status, form):
        self.status = status
        self.form = form


p1 = Human(name = 'Roma', age = 25, height = 178)
p2 = Human(name = 'Kostia', age = 29, height = 183)

print(p1.__dict__)
print(p2.__dict__)

s1 = Student(status='active', form='day')

print(s1.__dict__)





