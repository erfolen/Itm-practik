#Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.
# Координаты задаются пользователем, например (10, 15).

coordinats= input('Введите координаты через запятую x,у; пример:10, 15: ')
coordinats = coordinats.split(',')
try:
    x = int(coordinats[0])
    y = int(coordinats[1])

    if x > 0:
        print('I четверть' if y > 0 else 'IV четверть')
    else:
        print('II четверть' if y > 0 else 'III четверть')
except Exception as e:
    print("Вы ввели не правильные данные")
    print(e)

