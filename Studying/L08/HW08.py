#створити класс тварина щоб атрибут вік не міг бути
# менший нуля і більший 50 використовуючи property


class Animal:

    def __init__(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 50 and value > 0:
            self.__age = value

    age = property(get_age, set_age)

animal = Animal(50)
animal.age = 53
print(animal.age)
