class I:

    def __init__(self, lim):
        self.lim = lim
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.lim:
            self.count +=1
            return self.count
        else:
            raise StopIteration

# a = I(6)
# #
# # for i in a:
# #     print(i)