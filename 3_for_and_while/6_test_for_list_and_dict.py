# Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте тоже самое со словарем и выведите ключ и значение

my_list = fruits = ["Яблоко", "Банан", "Апельсин", "Груша", "Виноград", "Киви", "Манго", "Ананас", "Клубника", "Черешня", "Арбуз", "Персик", "Гранат", "Лимон", "Лайм"]
fruits_colors = {
    "Яблоко": "Красное",
    "Банан": "Желтый",
    "Апельсин": "Оранжевый",
    "Груша": "Зеленый",
    "Виноград": "Фиолетовый",
    "Киви": "Коричневый",
    "Манго": "Желтый",
    "Ананас": "Желтый",
    "Клубника": "Красный",
    "Черешня": "Красный",
    "Арбуз": "Зеленый",
    "Персик": "Оранжевый",
    "Гранат": "Красный",
    "Лимон": "Желтый",
    "Лайм": "Зеленый"
}

# Вывод списка фруктов

for i in my_list:
    print(i, end=' ')

print('\n'*2, '*'*100, '\n')


# выводи key и value

for key, item in fruits_colors.items():
    print(f'{key} --- {item}')