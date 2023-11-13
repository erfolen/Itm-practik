#error ZeroDivisionError
# print(5/0)

try:
    print(5 / 0)
except ZeroDivisionError:
    print('На ноль делить нельзя')