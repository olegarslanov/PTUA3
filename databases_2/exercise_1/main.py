import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///projektas_exercise1.db")
Base = declarative_base()


class Projektas(Base):
    __tablename__ = "Employes"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    born_date = Column("Gimimo data", String)
    position = Column("Pareigos", String)
    salary = Column("Atlyginimas", Float)
    start_work_date = Column(
        "Nuo kada dirba", DateTime, default=datetime.datetime.utcnow
    )

    def __init__(self, name, surname, born_date, position, salary):
        self.name = name
        self.surname = surname
        self.born_date = born_date
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.id} {self.name} {self.surname} {self.born_date} {self.position} {self.salary} {self.start_work_date}"


Base.metadata.create_all(engine)
