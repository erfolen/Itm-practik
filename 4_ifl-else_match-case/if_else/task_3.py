# Даны два числа. Вывести вначале большее, а затем меньшее из них.
try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))

    print(first_number, second_number) if first_number > second_number else print(second_number, first_number)

except Exception as e:
    print("Вы ввели не число")
    print(e)
