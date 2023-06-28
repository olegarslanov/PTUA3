# Create a TO DO list application that runs in terminal. It should allow user to log in.
# Each user should have his own tasks in to do list. User should be able to add/ update/
# delete tasks. User information and task information should be kept in database

# Nutariau naudoti one2many metoda, sukurti lenteliu sablonai

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# создаем подключение к базе данных
engine = create_engine("sqlite:///user_tasks.db")
# создаем экземпляр класса declarative_base (rysiai tarp musu lenteliu)
Base = declarative_base()


# определяем модель для таблицы User
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    password = Column("Password", String)
    tasks = relationship("Task", back_populates="user")

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.id} {self.name} {self.surname} {self.email} {self.password}"


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column("Title", String)
    description = Column("Description", String)
    deadline = Column("Deadline", String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

    def __init__(self, title, description, deadline, user_id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.user_id = user_id

    def __repr__(self):
        return (
            f"{self.id} {self.title} {self.description} {self.deadline} {self.user_id}"
        )


# создаем таблицы в базе данных
Base.metadata.create_all(engine)
