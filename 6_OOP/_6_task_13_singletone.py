class GovtSingleton:
    __instance__ = None

    def __init__(self):
        if GovtSingleton.__instance__ is None:
            GovtSingleton.__instance__ = self
        else:
            raise Exception('Create another class')

    @staticmethod
    def get_instance():
        if not GovtSingleton.__instance__:
            GovtSingletonleton()
        return GovtSingleton.__instance__


class Singleton_2:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance



if __name__ == '__main__':
    govt = GovtSingleton()
    print(govt)

    print(govt.get_instance())

    a = Singleton_2()
    b = Singleton_2()
    print(a, b, sep='\n')
