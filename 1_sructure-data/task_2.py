# задача 1
# Дано расстояние L в сантиметрах. Используя операцию деления нацело,
# найти количество полных метров в нем (1 метр = 100 см).

def long_m(l):
    return l // 100


# задача 2
# Дана масса M в килограммах. Используя операцию деления нацело,
# найти количество полных тонн в ней (1 тонна = 1000 кг).

def massa_kg(m):
    return m // 1000


# задача 3
# Дан размер файла в байтах. Используя операцию деления нацело,
# найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).

def size_f(a):
    return a // 1024


# задача 4
# Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально
# возможное количество отрезков длины B (без наложений). Используя операцию деления нацело,
# найти количество отрезков B, размещенных на отрезке A.

def count_line(a, b):
    return a // b


# задача 5
# Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально
# возможное количество отрезков длины B (без наложений). Используя операцию взятия остатка от деления нацело,
# найти длину незанятой части отрезка A.

def count_line_ostat(a, b):
    return a % b


# задача 6
# Дано двузначное число. Вывести вначале его левую цифру (десятки),
# а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию деления нацело,
# для нахождения единиц — операцию взятия остатка от деления.

def num_2(n):
    print(n // 10, n % 10)


# задача 7
# Дано двузначное число. Найти сумму и произведение его цифр.

def num_calcul(n):
    a = n // 10
    b = n % 10
    print(a + b, a * b)


# задача 8
# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.

def num_revers(n):
    a = n // 10
    b = n % 10
    return b * 10 + a


# задача 9
# Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).

def num_3_out_1(n):
    n // 100


# задача 10
# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).

def num_3_out_lm(n):
    a = n % 10
    b = n // 10 % 10
    print(a * 10 + b)
