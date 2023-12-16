class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y


class Multiplication(Calculator):
    def sum(self):
        return str(self.x) + str(self.y)


if __name__ == '__main__':
    calc = Calculator(2, 5)
    print(calc.sum())
    calc_2 = Multiplication(3, 7)
    print(calc_2.sum())
