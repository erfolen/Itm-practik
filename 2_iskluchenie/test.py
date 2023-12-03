import logging

my_logger = logging.getLogger('my')
#logging.basicConfig(level='DEBUG', filename='error.log')
my_logger.setLevel('DEBUG')

my_handler = logging.FileHandler('error.')
my_format = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

my_handler.setFormatter(my_format)
my_logger.addHandler(my_handler)

class MyError(Exception):
    pass





def main():
    a = 5 + 6
    raise MyError('test')


if __name__ == '__main__':
    main()
