#*** Реализуйте программу калькулятор.
# На вход подается три значения: первое число, второе число и операция( *, /, + или -) .
# На выходе должны получить число, после выполнения операции.

def main():
    try:
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
        operator = input('Введите операцию: ')

        match operator:
            case '+':
                print(first_number + second_number)
            case '-':
                print(first_number - second_number)
            case '*':
                print(first_number * second_number)
            case '/':
                print(first_number / second_number)
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except Exception as e:
        print("Вы ввели не число")
        print(e)

if __name__ == '__main__':
    main()

