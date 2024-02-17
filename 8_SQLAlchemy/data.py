from models import Employees, Shippers, Supplies, Products, Customers, Orders

employees_data_1 = Employees(
    last_name='Потребенко', first_name='Елена', surname='Владимировна', job_title='Специалист по продажам',
    address='пр-т Партизанский, 35', home_phone='37529151', dob='1991-01-01'
)

employees_data_2 = Employees(
    last_name='Колков', first_name='Тимофей', surname='Васильевич', job_title='Специалист по продажам',
    address='ул. Гикевича, 12', home_phone='37529082121', dob='1981-11-11'
)
employees_data_3 = Employees(
    last_name='Корженевский', first_name='Андрей', surname='Тадеушевич', job_title='Специалист по продажам',
    address='пр-т Московский, 7', home_phone='375445821104', dob='1985-07-07'
)
employees_data_4 = Employees(
    last_name='Федосов', first_name='Олег', surname='Игоревич', job_title='Кладовщик',
    address='ул. Куйбышева, 23', home_phone='375291910627', dob='1983-09-09'
)
employees_data_5 = Employees(
    last_name='Полянская', first_name='Светлана', surname='Геннадьевна', job_title='Юрисконсульт',
    address='пр-т Независимости, 50', home_phone='375295722020', dob='1989-03-03'
)
employees_data_6 = Employees(
    last_name='Тен', first_name='Михаил', surname='Викторович', job_title='Специалист по продажам',
    address='ул. Первомайская, 14', home_phone='37529101062', dob='1978-02-14'
)

employees_data = [employees_data_1, employees_data_2, employees_data_3,
                  employees_data_4, employees_data_5, employees_data_6, ]

shippers_data_1 = Shippers(
    name='ООО "БелЭкспрессЛогистика"', agent='Иванова Наталья Сергеевна', fio='Васильев Владимир Николаевич',
    phone='+375296789012', address='пр. Советский, д. 6, г. Гомель',
)
shippers_data_2 = Shippers(
    name='Транспортная компания "БелЛайн"', agent='Кузнецов Сергей Алексеевич', fio='Андреева Ольга Андреевна',
    phone='+375295678901', address='ул. Ленина, д. 5, г. Витебск',
)
shippers_data_3 = Shippers(
    name='ООО "БелТрансСервис"', agent='Сергеева Мария Игоревна', fio='Никитин Алексей Дмитриевич',
    phone='+375294567890', address='пр. Гагарина, д. 4, г. Могилёв',
)
shippers_data_4 = Shippers(
    name='Логистическая фирма "БелЛогист"', agent='Федоров Павел Владимирович', fio='Кузнецова Екатерина Алексеевна',
    phone='+375293456789', address='ул. Советская, д. 3, г. Брест',
)
shippers_data_5 = Shippers(
    name='Транспортная компания "ТрансБел"', agent='Смирнова Анастасия Петровна', fio='Сидоров Иван Александрович',
    phone='+375292345678', address='пр. Ленина, д. 2, г. Гродно',
)
shippers_data_6 = Shippers(
    name='ООО "БелТрансЛогистика"', agent='Иванов Иван Иванович', fio='Петров Петр Петрович', phone='+375291234567',
    address='ул. Гагарина, д. 1, г. Минск',
)

shippers_data = [shippers_data_1, shippers_data_2, shippers_data_3, shippers_data_4, shippers_data_5, shippers_data_6]

supplies_data_1 = Supplies(
    shippers_id='1', delivery_date='2023-01-05'
)
supplies_data_2 = Supplies(
    shippers_id=1, delivery_date='2023-02-12'
)
supplies_data_3 = Supplies(
    shippers_id=2, delivery_date='2023-03-2'
)
supplies_data_4 = Supplies(
    shippers_id=3, delivery_date='2023-06-08'
)
supplies_data_5 = Supplies(
    shippers_id=4, delivery_date='2023-08-19'
)
supplies_data_6 = Supplies(
    shippers_id=5, delivery_date='2023-09-03'
)

supplies_data = [supplies_data_1, supplies_data_2, supplies_data_3, supplies_data_4, supplies_data_5, supplies_data_6]

product_data_1 = Products(
    supplies_id=1, name='ИК обогреватель KALASHNIKOV KIRH-E10T-11 с открытым излучателем',
    specifications='ехнические характеристики|Мощность, кВт|1,0 Технические характеристики|Высота установки, '
                   'м|2,4 - 3,5 Технические характеристики|Размер, мм|935*42*110',
    description='Принцип действия отличается от другого теплового оборудования — он нагревает предметы, '
                'а не воздух и из этого вытекает ряд преимуществ:<— можно обогреваться '
                'на открытом пространстве<— не сжигает кислород',
    images='catalog/i/hi/ea/10450278471a65389177859830d337b8.jpg', cost=950.20, quantity=15, price=1377.79
)
product_data_2 = Products(
    supplies_id=1, name='ИК обогреватель KALASHNIKOV KIRH-E08P-11',
    specifications='Технические характеристики|Обслуживаемая площадь, м2|8 Технические характеристики|'
                   'Излучающая панель|есть Технические характеристики|Вес с коробкой, кг|4,4 Т',
    description='Инфракрасный излучатель KIRH-E08P-11 генерирует тепло и направляет его не на обогрев воздуха, '
                'как всё остальное климатическое оборудование, а подобно солнечным лучам —на обогрев предметов и '
                'поверхностей. Агрегат 0,8 кВт предназначен для обогрева помещения 8-16 м2 ',
    images='catalog/i/fk/pk/e735fce7cc01ef51ca3a2836a8eebb7d.jpg', cost=1354.42, quantity=15, price=1963.91
)
product_data_3 = Products(
    supplies_id=2, name='ИК обогреватель KALASHNIKOV KIRH-E08P-11',
    specifications='ехнические характеристики|Мощность, кВт|0,8 Технические характеристики|Высота установки, м'
                   '|2,4 - 3,5 Технические характеристики|Размер, мм|1190*42*130 ',
    description='Инфракрасный излучатель KIRH-E08P-11 генерирует тепло и направляет его не на обогрев воздуха,'
                ' как всё остальное климатическое оборудование, а подобно солнечным лучам —на обогрев предметов '
                'и поверхностей. Агрегат 0,8 кВт предназначен для обогрева помещения 8-16 м2 ',
    images='catalog/i/fk/pk/e735fce7cc01ef51ca3a2836a8eebb7d.jpg', cost=1390.00, quantity=15, price=2015.50
)
product_data_4 = Products(
    supplies_id=3, name='Кондиционер Energolux Basel SAS12B3-A/SAU12B3-A',
    specifications='Конструкция|Хладагент|R 410A Управление|Wi-Fi|поддерживается, модуль отдельно приобретается '
                   'Основные|Гарантия|7 лет Основные|Тип кондиционера',
    description='Белоснежное глянцевоепокрытиена кондиционерахEnergoluxBasel SAS12B3-A/SA12B3-Aотличает его от '
                'других серий, а классика дизайна прекрасно впишется в любую комнату. Сплит-система укомплектована '
                'достаточно удобным многофункциональным русскоязычным пультом ДУ',
    images='catalog/vodonagrevateli/energoljuks/dizajnbeznazvanija-2023-01-16t134139.874.jpg',
    cost=124.17, quantity=4, price=180.05
)
product_data_5 = Products(
    supplies_id=4, name='Кондиционер Energolux Basel SAS12B3-A/SAU12B3-A',
    specifications='Конструкция|Хладагент|R 410A Управление|Wi-Fi|поддерживается, модуль отдельно приобретается '
                   'Основные|Гарантия|7 лет Основные|Тип кондиционера|сплит-система',
    description='Белоснежное глянцевоепокрытиена кондиционерахEnergoluxBasel SAS12B3-A/SA12B3-Aотличает его от '
                'других серий, а классика дизайна прекрасно впишется в любую комнату. Сплит-система укомплектована '
                'достаточно удобным многофункциональным русскоязычным пультом ДУ',
    images='catalog/vodonagrevateli/energoljuks/dizajnbeznazvanija-2023-01-16t134139.874.jpg',
    cost=110.00, quantity=4, price=159.50
)
product_data_6 = Products(
    supplies_id=5, name='Кондиционер Energolux Basel SAS07B3-A/SAU07B3-A',
    specifications='Конструкция|Хладагент|R 410A Управление|Wi-Fi|поддерживается, модуль отдельно приобретается '
                   'Основные|Гарантия|7 лет Основные|Тип кондиционера|',
    description='Белоснежное глянцевоепокрытиена кондиционерахEnergoluxBasel SAS07B3-A/SAU07B3-Aотличает его от '
                'других серий, а классика дизайна прекрасно впишется в любую комнату. Сплит-система укомплектована '
                'достаточно удобным многофункциональным русскоязычным пультом ДУ',
    images='catalog/vodonagrevateli/energoljuks/dizajnbeznazvanija-2023-01-16t134139.874.jpg',
    cost=143.68, quantity=15, price=208.34
)

products_data = [product_data_1, product_data_2, product_data_3, product_data_4, product_data_5, product_data_6]

customer_data_1 = Customers(
    fio='Александр Булаш', address='ул. Могилевская, 4-4-67 ', phone='+375297780235',
)
customer_data_2 = Customers(
    fio='Александр Шашкин', address='Коссовский Тракт Д.82 Кв.75', phone='375298097446',
)
customer_data_3 = Customers(
    fio='Виктор Кондратчик', address='Лесная 2', phone='80333102103',
)
customer_data_4 = Customers(
    fio='Наталья  Савченко', address='Широкая 34 ком 817', phone='+375298472543',
)
customer_data_5 = Customers(
    fio='Олег Букатин', address='Волгоградская ул.10 - 15', phone='375296362483',
)
customer_data_6 = Customers(
    fio='Евгения Симакова', address= 'Ул. Павлины Меделки, 3-98', phone='+375295045206',
)
customer_data_7 = Customers(
    fio='Анна Савицкая', address='Минск, Ольшевского 24, 4 этаж, 419 офис', phone='375291684757',
)

customers_data = [customer_data_1, customer_data_2, customer_data_3, customer_data_4, customer_data_5, customer_data_6,
                  customer_data_7]

order_data_1 = Orders(
    employees_id=1, products_id=1, customers_id=1, date_create='2023-12-06', date_did_order='2023-12-08',
)

order_data_2 = Orders(
    employees_id='1', products_id='2', date_create='2023-12-07', date_did_order='2023-12-09', customers_id='2',
)

order_data_3 = Orders(
    employees_id='2', products_id='3', date_create='2023-12-08', date_did_order='2023-12-10', customers_id='3',
)

order_data_4 = Orders(
    employees_id='3', products_id='4', date_create='2023-12-09', date_did_order='2023-12-11', customers_id='4',
)
order_data_5 = Orders(
    employees_id='4', products_id='5',date_create='2023-12-10', date_did_order='2023-12-12', customers_id='5',
)
order_data_6 = Orders(
    employees_id='5', products_id='5', date_create='2023-12-11', date_did_order='2023-12-13', customers_id='5',
)

orders_data = [order_data_1, order_data_2, order_data_3, order_data_4, order_data_5, order_data_6]
