from models import Employees



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
                  employees_data_4, employees_data_5, employees_data_6,]
