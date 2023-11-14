# Напишите программу для вывода таблицы умножения от 0 до 9.
# 0*1 = 0
# 0 *2 = 0

for i in range(10):
    for j in range(10):
        res = i * j
        print(f'{i}*{j} = {res}')
    print('-'*20)    