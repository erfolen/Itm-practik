import logging


my_logger = logging.getLogger('my_exception')
my_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика
my_handler = logging.FileHandler("error.log")    #mode='w' - перезаписывает файл
my_format = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
my_handler.setFormatter(my_format)

# добавление обработчика к логгеру
my_logger.addHandler(my_handler)




class CustomError(Exception):
    """ Собственное исключение отрицательных чисел"""

    def __init__(self, val):
        self.val = val
        massage = f"значение не должно быть отрицательное, передали: {self.val}"
        super().__init__(massage)


# пример использование собсвенного исключение с помощью riese
def positive_value(v):
    if v < 0:
        my_logger.info(f'значение отрицательное, {v}')
        raise CustomError(v)
    else:
        print(f'передали положительное значения: {v}')


try:
    my_logger.info('start kod')
    positive_value(15)
    positive_value(-2)
except CustomError as ce:
    print(f'исключение {ce}')
    my_logger.error(ce)
finally:
    print('Всегда срабатывает')
    my_logger.info('end')
