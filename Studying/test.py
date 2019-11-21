class Paper(object):

    def __init__(self,count):
        self.count = count

    def load(self,q):
        if q > 0:
            self.count = q

    def get_count(self):
        return self.count

    def draw(self,text):
        if self.count > 0:
            self.count -=1
        print(text)

class Printer(object):

    def error(self, msg):
        print(msg)

    def print(self,paper,text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('Error')
            print('paper q-ty is ', paper.get_count())

class Facade(object):

    def __init__(self):
        self.printer = Printer()
        self.paper = Paper(2)

    def write(self,text):
        self.printer.print(self.paper,text)

    def load(self,q):
        self.paper.load(q)
        print(self.paper.count)



f = Facade()

f.write('Hello world')
f.write('How are  you ?')
f.write('I`m fine')
f.load(3)
f.write('Hfgsdfg')
f.write('Hffddfg')
print(f.paper.count)
