#Дано целое число в диапазоне 100–999.
# Вывести строку-описание данного числа, например: 256 — «двести пятьдесят шесть»,
# 814 — «восемьсот четырнадцать».

def main():
    number = int(input('Введите число:  '))
    h = number // 100
    d = (number - h * 100) // 10
    e = number - h * 100 - d * 10
    strok_number = ''

    match h:
        case 1:
            strok_number += 'сто '
        case 2:
            strok_number += 'двесте '
        case 3:
            strok_number += 'триста '
        case 4:
            strok_number += 'четыриста '
        case 5:
            strok_number += 'пятьсот '
        case 6:
            strok_number += 'шестьсот '
        case 7:
            strok_number += 'семьсот '
        case 8:
            strok_number += 'восемьсот '
        case 9:
            strok_number += 'девятсот '

    match d:
        case 1:
            match e:
                case 1:
                    return print(strok_number + 'одиннадцать')
                case 2:
                    return print(strok_number + 'двеннадцать')
                case 3:
                    return print(strok_number + 'триннадцать')
                case 4:
                    return print(strok_number + 'четырнадцать')
                case 5:
                    return print(strok_number + 'пятнадцать')
                case 6:
                    return print(strok_number + 'шестнадцать')
                case 7:
                    return print(strok_number + 'семьнадцать')
                case 8:
                    return print(strok_number + 'восемьнадцать')
                case 9:
                    return print(strok_number + 'девятнадцать')
                case 0:
                    return print(strok_number + 'десять')
        case 2:
            strok_number += 'двадцать'
        case 3:
            strok_number += 'тридцать'
        case 4:
            strok_number += 'сорок'
        case 5:
            strok_number += 'пятьдесят'
        case 6:
            strok_number += 'шестьдесят'
        case 7:
            strok_number += 'семьдесят'
        case 8:
            strok_number += 'восемьдесят'
        case 9:
            strok_number += 'девяносто'

    match e:
        case 1:
            strok_number += ' один'
        case 2:
            strok_number += ' два'
        case 3:
            strok_number += ' три'
        case 4:
            strok_number += ' четыре'
        case 5:
            strok_number += ' пять'
        case 6:
            strok_number += ' шесть'
        case 7:
            strok_number += ' семь'
        case 8:
            strok_number += ' восемь'
        case 9:
            strok_number += ' девять'

    print(strok_number)


if __name__ == '__main__':
    main()
