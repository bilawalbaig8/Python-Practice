from ClassA import A


class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.__c = c

    def show(self):
        A.show(self)
        print("This is Class C")

    def getC(self):
        return self.__c
