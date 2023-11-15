try:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))
except Exception as e:
    print("Вы ввели не число")
    print(e)
