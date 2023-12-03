import time

class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self  # Возвращаем объект, который будет связан с переменной в блоке with

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Время выполнения: {elapsed_time} секунд")

# Использование контекстного менеджера для замера времени выполнения
with TimerContextManager() as timer:
    # Блок кода, для которого измеряется время выполнения
    for _ in range(1000000):
        pass  # просто проход по циклу
