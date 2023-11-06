# задача 1
def perim_kvad(a):
    return 4 * a


# задача 2
def s_kvad(a):
    return a ** 2


# задача 3
class Figura:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perim(self):
        return 2 * (self.a + self.b)

    def squre(self):
        return self.a * self.b


# задача 4
import math


def diametr_okr(d):
    return math.pi * d


# задача 5
# Дана длина ребра куба a. Найти объем куба V = a3
# и площадь его поверхности S = 6·a2
class Figura_kub:
    def __init__(self, a):
        self.a = a

    def v_kub(self):
        return self.a ** 3

    def s_poverchnost(self):
        return 6 * self.a ** 2


# задача 6
# Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

class Figura_pram:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def v_pram(self):
        return self.a * self.b * self.c

    def s_poverhnost(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)


# задача 7
# Найти длину окружности L и площадь круга S заданного радиуса R:
# L = 2·π·R, S = π·R2, π=3.14

class Figura_krug:
    def __init__(self, r):
        self.r = r

    def long_krug(self):
        return 2 * math.pi * self.r

    def s_krug(self):
        return math.pi * self.r ** 2


# задача 8
# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

def average_value(a, b):
    return (a + b) / 2


# задача 9
# Даны два неотрицательных числа a и b.
# Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a·b)1/2

def average_geometria(a, b):
    return (a * b) ** (1 / 2)


# задача 10
# Даны два ненулевых числа.
# Найти сумму, разность, произведение и частное их квадратов.

class Calculator_num:
    def __init__(self, x, y):
        self.x = x ** 2
        self.y = y ** 2

    def sum(self):
        return self.x + self.y

    def difference(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y
