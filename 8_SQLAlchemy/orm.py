from database import Base, engine, session_fabric
from sqlalchemy import select, join
from sqlalchemy.orm import selectinload

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
    def join_table(table, join_table):
        '''SELECT * FROM supplies INNER JOIN shippers ON supplies.shippers_id = shippers.id ;'''
        with session_fabric() as session:
            query = select(table).options(selectinload(join_table))
            # query = select(table).join(join_table)
            result = session.execute(query)
            print(query)
            return result.scalars().all()



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

