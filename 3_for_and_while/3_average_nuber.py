# Напишите программу для подсчета среднего числа всех введенных пользователям чисел.
average = 0
count = 0

while True:
    try:
        number = int(input("Введите числи для подсчета среднего числа, если хотите получить результат введите 0:  "))

        if number == 0:
            break
        else:
            average += number
            count += 1
    except:
        print('Вы ввели не число')

print(average / count)
