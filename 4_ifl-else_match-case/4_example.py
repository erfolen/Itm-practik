import random


def main():
    num = random.randint(0, 10)
    while True:
        try:
            num_user = int(input('Угадайте число от 0 до 10:  '))
            if num_user == num:
                print(f'Ура ты угадал число: {num_user}')
                break
            elif num > num_user:
                print(f'ты не угадал число: введи число больше {num_user}')
            elif num < num_user:
                print(f'ты не угадал число: введи число меньше {num_user}')
        except Exception as e:
            print("Вы ввели не число")
if __name__ == '__main__':
    main()