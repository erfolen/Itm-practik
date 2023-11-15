#Даны три числа. Найти наименьшее из них.

try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))

    if first_number > second_number and first_number > third_number:
        print(first_number)
    elif second_number > third_number:
        print(second_number)
    else:
        print(third_number)

except Exception as e:
    print("Вы ввели не число")
    print(e)
