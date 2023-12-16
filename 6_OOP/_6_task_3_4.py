class MeansOfTransport:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def show_color(self):
        print(self.color)

    def show_brand(self):
        print(self.model)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_brand(self):
        return self.model

    def set_brand(self, brand):
        self.model = brand


if __name__ == '__main__':
    car = MeansOfTransport('red', 'BMW')
    car.show_color()
    car.show_brand()
    print(car.get_brand(), car.get_color())