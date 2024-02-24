from database import Base, engine, session_fabric
from sqlalchemy import select, join, func, distinct, delete
from sqlalchemy.orm import selectinload
from models import Orders, Employees, Customers, Products, Shippers


class ActionsDB:
    @staticmethod
    def create_table():
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_data_all(data):
        with session_fabric() as session:
            session.add_all(data)
            session.commit()

    @staticmethod
    def insert_data_one(data):
        with session_fabric() as session:
            session.add(data)
            session.commit()

    @staticmethod
    def select_all_table(orm_model):
        with session_fabric() as session:
            query = select(orm_model)
            result = session.execute(query)
            return result.scalars().all()

    @staticmethod
    def join_table(table, tab2):
        '''SELECT * FROM supplies INNER JOIN shippers ON supplies.shippers_id = shippers.id ;'''
        with session_fabric() as session:
            # query = select(table, tab2).options(selectinload(tab2))
            query = select(table, tab2).join(tab2)
            result = session.execute(query)
            return result.all()

    @staticmethod
    def where_table_name_employees(name):
        with session_fabric() as session:
            query = select(Employees).filter(Employees.first_name == name)
            result = session.execute(query).scalars().all()
            return result

    @staticmethod
    def order_by_employess():
        """SELECT * FROM employees ORDER BY last_name, first_name;"""
        with session_fabric() as session:
            query = select(Employees).order_by(Employees.last_name, Employees.first_name)
            return session.execute(query).scalars().all()

    @staticmethod
    def update_table_phone(table, table_id, new_date):
        with session_fabric() as session:
            table_row = session.get(table, table_id)
            table_row.phone = new_date
            session.commit()

    @staticmethod
    def group_by_employees():
        with session_fabric() as session:
            query = select(Employees.last_name, func.count(Employees.id)).join(Orders).group_by(Employees.id, Employees.last_name)
            return session.execute(query).all()

    @staticmethod
    def distinct_table_products():
        with session_fabric() as session:
            query = select(Products.name).distinct()
            return session.execute(query).all()

    @staticmethod
    def max_price_product():
        with session_fabric() as session:
            query = select(func.max(Products.price))
            return session.execute(query).scalar()

    @staticmethod
    def delete_shippers(name):
        with session_fabric() as session:
            session.query(Shippers).filter(Shippers.name == name).delete()
            session.commit()

    @staticmethod
    def drop_table():
        Base.metadata.drop_all(engine)

    @staticmethod
    def print_properties(obj):
        for i in obj:
            print('*' * 20)
            for prop in vars(i).items():
                if prop[0] != '_sa_instance_state':
                    print(f'{prop[0]} = {prop[1]}')
