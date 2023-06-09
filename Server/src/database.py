from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .utils import Singleton

Model = declarative_base(name='Model')


class Database(Singleton):
    def __init__(self):
        self.engine = create_engine(
            'mysql+mysqlconnector://root:delfi123@localhost:3306/tickets')
        self.session = sessionmaker(bind=self.engine)
        Model.metadata.create_all(self.engine)

    def get_database(self):
        return self.session()
