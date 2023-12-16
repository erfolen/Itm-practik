from abc import ABC, abstractmethod


class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass


class Cat(Animals):
    def voice(self):
        print('May')



if __name__ == '__main__':
    cat = Cat()
    cat.voice()
