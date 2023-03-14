from ClassB import B
from ClassC import C


class D(B, C):
    def __init__(self, a, b, c, d):
        B.__init__(self, a, b)
        C.__init__(self, a, c)
        self.__d = d

    def show(self):
        B.show(self)
        C.show(self)
        print("This is Class D")

    def getD(self):
        return self.__d
