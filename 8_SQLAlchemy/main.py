from orm import ActionsDB
from data import employees_data, shippers_data, supplies_data, products_data, customers_data, orders_data

if __name__ == '__main__':
    ActionsDB.drop_table()
    ActionsDB.create_table()
    # # ActionsDB.insert_data_one(employees_data_1)
    # # ActionsDB.insert_data_all([employees_data_2, employees_data_3,
    # employees_data_4, employees_data_5, employees_data_6])
    ActionsDB.insert_data_all(employees_data)
    ActionsDB.insert_data_all(shippers_data)
    ActionsDB.insert_data_all(supplies_data)
    ActionsDB.insert_data_all(products_data)
    ActionsDB.insert_data_all(customers_data)
    ActionsDB.insert_data_all(orders_data)
