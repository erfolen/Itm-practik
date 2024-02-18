from orm import ActionsDB
from data import employees_data, shippers_data, supplies_data, products_data, customers_data, orders_data
from models import Employees, Shippers, Supplies, Products, Customers, Orders

if __name__ == '__main__':
    # ActionsDB.drop_table()
    # ActionsDB.create_table()
    # # ActionsDB.insert_data_one(employees_data_1)
    # # ActionsDB.insert_data_all([employees_data_2, employees_data_3,
    # employees_data_4, employees_data_5, employees_data_6])
    # ActionsDB.insert_data_all(employees_data)
    # ActionsDB.insert_data_all(shippers_data)
    # ActionsDB.insert_data_all(supplies_data)
    # ActionsDB.insert_data_all(products_data)
    # ActionsDB.insert_data_all(customers_data)
    # ActionsDB.insert_data_all(orders_data)
    employees = ActionsDB.select_all_table(Employees)
    ActionsDB.print_properties(employees)
    shippers = ActionsDB.select_all_table(Shippers)
    ActionsDB.print_properties(shippers)
    supplies = ActionsDB.select_all_table(Supplies)
    ActionsDB.print_properties(supplies)
    products = ActionsDB.select_all_table(Products)
    ActionsDB.print_properties(products)
    customers = ActionsDB.select_all_table(Customers)
    ActionsDB.print_properties(customers)
    orders = ActionsDB.select_all_table(Orders)
    ActionsDB.print_properties(orders)

