class A:

    def __init__(self,lim):
        self.lim = lim
        self.a = 0
        self.b = 1


    def __iter__(self):
        return self


    def __next__(self):
        fib = self.a

        if fib > self.lim:
            raise StopIteration

        self.a, self.b = self.b, self.a + self.b

        return fib

## a = A(100)
##
## for i in a:
##     print(i)