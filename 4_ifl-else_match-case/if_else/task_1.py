# Даны три целых числа. Найти количество положительных чисел в исходном наборе.
try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))

    if first_number > 0 and second_number > 0 and third_number > 0:
        print(f'Вы ввели 3 положительных числа')
    # elif (first_number > 0 and second_number > 0) or (first_number > 0 and third_number > 0) or (second_number > 0 and third_number > 0):
    elif (first_number > 0 and (second_number > 0 or third_number > 0)) or (second_number > 0 and third_number > 0):
        print(f'Вы ввели 2 положительных числа')
    elif first_number > 0 or second_number > 0 or third_number > 0:
        print(f'Вы ввели 1 положительное число')
    else:
        print('Вы ввели ни одного положительного числа')
except Exception as e:
    print("Вы ввели не число")
    print(e)
