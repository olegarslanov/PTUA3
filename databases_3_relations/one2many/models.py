from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# создаем подключение к базе данных
engine = create_engine("sqlite:///one2many_test.db")
# создаем экземпляр класса declarative_base
Base = declarative_base()


# определяем модель для таблицы tevas
class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikai = relationship("Vaikas", back_populates="tevas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)
    tevas_id = Column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas", back_populates="vaikai")


# создаем таблицы в базе данных
Base.metadata.create_all(engine)
