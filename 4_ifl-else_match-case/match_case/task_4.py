# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток) и
# принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.

def main():
    N = input('Введите направления робота: ')
    com_rob = input('Введите команда для робота:  ')
    napr = 'СЗЮВ'
    result_com = 0
    start_n = 0

    match N:
        case 'С':
            start_n = 0
        case 'З':
            start_n = 1
        case 'Ю':
           start_n = 2
        case 'В':
            start_n = 3

    for i in com_rob:
        match i:
            case '-':
                result_com = result_com - 2
            case '1':
                result_com = result_com + 1
    result_com = (start_n + result_com) % 4 + 1

    print(napr[result_com])


if __name__ == '__main__':
    main()