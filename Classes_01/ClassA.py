class A:
    def __init__(self, a, b):
        self.__a = a
        self.b = b

    def show(self):
        print("these variables are in Class A : ", self.__a, self.b)

    def sum(self):
        return self.__a + self.b

    def get_a(self):
        a = self.__a
        return a
