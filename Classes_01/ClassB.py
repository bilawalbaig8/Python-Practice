from ClassA import A


class B (A):
    def __init__(self, a1, b1, c):
        super().__init__(a1, b1)
        self.c = c

    def show(self):
        super().show()
        print("This is Class B :", self.c)

    def sum(self):
        print(super().sum())
        print(self.c + super().sum())




