class Paranet:
    def __init__(self):
        self.parent_atribute = 'I am Parent'

    def parent_method(self):
        print('Method parent')


class Child(Paranet):
    def __init__(self):
        super().__init__()
        self.child_atribute = 'I am child'


class B:
    def x(self):
        print('x: B')


class C:
    def x(self):
        print('x: C')

class D(B, C):
    pass




if __name__ == '__main__':

    child = Child()
    print(child.parent_atribute)
    print(child.child_atribute)
    child.parent_method()

    d = D()
    d.x()
    print(D.mro())