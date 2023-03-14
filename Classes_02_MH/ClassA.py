class A:
    def __init__(self, a):
        self.__a = a

    def show(self):
        print("This is Class A")

    def getA(self):
        return self.__a

