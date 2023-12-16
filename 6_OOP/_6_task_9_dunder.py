class Car:
    key = '123456'

    @staticmethod
    def is_class(object_my):
        return True if isinstance(object_my, Car) else False

    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.power = 800
        self.option = [
            'Усилитель руля', 'Кондиционер', 'Стеклоподъемники', 'Защита картера двигателя',
            'Передние датчики парковки', 'Задние датчики парковки', 'Система контроля устойчивости ESP',
            'Центральный замок', 'Cигнализация', 'Иммобилайзер',
        ]
        self.index = 0

    def __getattribute__(self, item):
        if item == 'key':
            print('Нет доступа')
        return object.__getattribute__(self, item)

    def __setattr__(self, name, value):
        if name == 'model' and hasattr(self, name):
            print('Модель нельзя менять')
        else:
            super().__setattr__(name, value)

    def __delattr__(self, item):
        if item == 'key' or item == 'model' or item == 'color':
            print('Нельзя удалять')
        else:
            print(f'Вы удалили {item}')
            super().__delattr__(item)

    def __eq__(self, other):
        if self.is_class(other):
            return self.color == other
        if isinstance(other, str):
            return self.color == other

    def __lt__(self, other):
        if self.is_class(other):
            return self.power < other.power
        if isinstance(other, int):
            return self.power < other

    def __gt__(self, other):
        return not __lt__(self, other)

    def __add__(self, other):
        return self.power + other.power

    def __radd__(self, other):
        return other + self.power

    def __str__(self):
        return 'Создания автомобиля'

    def __repr__(self):
        return f'Класс: {self.__class__.__name__}, Атрибуты экземпляра: {self.__dict__}'

    # не работает так определен маг метод __eq__
    def __hash__(self):
        return hash((self.model, self.color, self.power))

    def __getitem__(self, item):
        return self.option[item]

    def __setitem__(self, index, value):
        self.option[index] = value

    def __delitem__(self, index):
        del self.option[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.option):
            item = self.option[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __len__(self):
        return len(self.option)


if __name__ == '__main__':
    car = Car('Mersedes', 'black')
    print(car.model, car.color)
    car.model = "BMW"
    car.color = 'red'
    key = car.key
    print(car.model, car.color)
    car.door = 4
    del car.door
    del car.model

    car_2 = Car('BMW', 'red')
    car_3 = Car('Opel', 'black')
    print(car == car_2)
    print(car == car_3)
    print(car_3 == 'black')
    car_3.power = 2000
    car_2.power = 5000
    print(car_3 < car_2)
    print(car_3 < 6000)
    print(car_2 + car_3)
    print(2000 + car_3)

    print(car)
    print(repr(car))
    print(repr(car_2))
    print(car == car_2)

    print(car[3])
    del car[3]
    print(car[3])
    car[3] = 'Защита картера двигателя'
    print(car.option)
    for i in car_2:
        print(i)
    print(len(car))

