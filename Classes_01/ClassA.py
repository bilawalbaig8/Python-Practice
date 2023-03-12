class A:
    def __init__(self, a, b):
        self.__a = a  # Made this variable private but didn't happen anything with the code functionality
        self.b = b

    def show(self):
        print("these variables are in Class A : ", self.__a, self.b)

    def sum(self):
        return self.__a + self.b
