from database import Base, engine, session_fabric


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
    def drop_table():
        Base.metadata.drop_all(engine)
