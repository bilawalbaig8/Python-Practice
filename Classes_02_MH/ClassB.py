from ClassA import A

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.__b = b

    def show(self):
        A.show(self)
        print("This is Class B")

    def getB(self):
        return self.__b

