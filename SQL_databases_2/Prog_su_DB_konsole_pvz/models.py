# Tam, kad sukurtume reikiamos struktūros duomenų bazę ir ja naudotumės, užtenka
# sukurti SQLAlchemy klasę ir ją paleisti.

import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()


class Project(Base):
    __tablename__ = "Projektas"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)
# class.object.method(argument)


# Этот код на Python использует библиотеку SQLAlchemy для создания таблицы "Projektas" в базе
# данных SQLite и определения модели "Project" с помощью класса "declarative_base()".

# Затем создается класс "Project", который содержит следующие атрибуты:

# "id": первичный ключ таблицы, тип данных Integer.
# "name": название проекта, тип данных String.
# "price": стоимость проекта, тип данных Float.
# "created_date": дата создания проекта, тип данных DateTime.
# Конструктор класса "init" инициализирует атрибуты "name" и "price" для нового объекта класса
# "Project".

# Метод "repr" возвращает строку, содержащую значения атрибутов "id", "name", "price" и
# "created_date" для объекта класса "Project".

# Затем создается экземпляр "engine" класса "create_engine", который создает соединение с
# базой данных SQLite и указывает путь к файлу базы данных.

# Далее создается объект "Base" класса "declarative_base", который будет использоваться для
# определения моделей таблиц базы данных.

# Наконец, метод "create_all" объекта "metadata" класса "Base" вызывается с аргументом "engine",
# чтобы создать таблицу "Projektas" в базе данных.
