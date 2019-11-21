
class A(object):

    def fire(self):
        Observer().alarm()

    def alarm(self):
        print('AAAAA')

class B(object):

    def fire(self):
        Observer().alarm()

    def alarm(self):
        print('BBBBB')

class C(object):

    def fire(self):
        Observer().alarm()

    def alarm(self):
        print('CCCCC')

class Observer(object):
    listeners = [A, B, C]

    def alarm(self):

        for listener in self.listeners:
            listener().alarm()



b = B()
b.fire()