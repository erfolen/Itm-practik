#Даны два целых числа: D (день) и M (месяц), определяющие правильную дату невисокосного года.
#Вывести значения D и M для даты, следующей за указанной.

def main():
    global del_m
    try:
        D = int(input('Введите день:  '))
        M = int(input('Введите месяц:  '))
        M = M % 12
        match M:
            case 1 | 3 | 5 | 7 | 8 | 10:
                del_m = 31
            case 4 | 6 | 9 | 11:
                del_m = 30
            case 2:
                del_m = 28
            case 0:
                M = 1
                del_m = 31
        M = D // del_m + M
        D = D % del_m + 1
        print(D, M)
    except Exception as e:
        print('')
        print(e)


if __name__ == '__main__':
    main()