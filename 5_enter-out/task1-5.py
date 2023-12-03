file = open('lorum.txt')
print(file.read())  # считывает весь файл
print('-' * 20)
file.seek(10)  # передвинут каретку
print(file.readline())  # считывает только строку
print('-' * 20)
file.close()

file_2 = open('lorum.txt', 'a+')
file_2.write('new_info\n')
file_2.write('too string\n')
print('*' * 20)
file_2.seek(2)
print(file_2.read(5))
file_2.close()

with open('lorum.txt', 'r+') as f:
    print(f.readlines())
