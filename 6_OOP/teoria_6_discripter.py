class Discriptor_value:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Poind3D:
    x = Discriptor_value()
    y = Discriptor_value()
    z = Discriptor_value()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



if __name__ == '__main__':
    cord = Poind3D(2, 3, 4)

    print(cord.__dict__)