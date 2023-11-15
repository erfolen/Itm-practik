# Даны два числа. Вывести большее из них.


try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))

    print(first_number if first_number > second_number else second_number)
except Exception as e:
    print("Вы ввели не число")
    print(e)