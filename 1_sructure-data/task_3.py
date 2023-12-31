# 1. Дано целое число A. Проверить истинность высказывания: «Число A является положительным»..

def num_is_numeric(n):
    return n > 0


# 2. Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».

def num_is_even(n):
    return n % 2 == 0


# 3. Дано целое число A. Проверить истинность высказывания: «Число A является четным».
def num_is_odd(n):
    return n % 2 != 0


# 4. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3».

def nums_ravenstvo(a, b):
    return a > 2 and b <= 3


# 5. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥ 0 или B < −2».

def nums_ravenstvo_2(a, b):
    return a >= 0 or b < -2


# 6. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Справедливо двойное неравенство A < B < _C_».

def nums_ravenstvo_3(a, b, c):
    return a < b and b < c


# 7. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Число B находится между числами A и _C_».

def num_is_between(a, b, c):
    return a < b and b < c


# 8. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».

def nums_is_odd(a, b):
    return a % 2 != 0 and b % 2 != 0


# 9. Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».

def nums_is_odd_or(a, b):
    return a % 2 != 0 or b % 2 != 0

# 10. Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное»

def nums_is_odd_or_2(a, b):
    return a % 2 != 0 or b % 2 != 0

