from _6_task_3_4 import MeansOfTransport as Mot


class Car(Mot):
    car_drive = 4

    def __init__(self, color, model, count_wheels):
        super().__init__(color, model)
        self.count_wheels = count_wheels
        self._mkpp = 5
        self.__tip_korob = 'mechanic'

    @classmethod
    def get_car_drive(cls):
        print(cls.car_drive)


class Moped(Mot):
    def __init__(self, color, model, count_wheels):
        super().__init__(color, model)
        self.count_wheels = count_wheels

    @staticmethod
    def time_duration(s, v):
        if v <= 0:
            raise 'скорость должна быть больше 0'
        return f'{s / v} ч'


if __name__ == '__main__':
    car = Car('blue', 'honda', 4)
    print(car.get_color(), car.get_brand(), car.count_wheels)
    moped = Moped('green', 'suzuki', 2)
    print(moped.color, moped.model, moped.count_wheels)
    print(moped.time_duration(10, 20))
    print(Moped.time_duration(100, 40))
    print(car._mkpp)
    # print(car.__tip_korob)
    # print(dir(car))
    print(car._Car__tip_korob)
    car.get_car_drive()
