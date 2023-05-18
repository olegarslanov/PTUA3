from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# создаем экземпляр класса declarative_base
Base = declarative_base()

# создаем подключение к базе данных
engine = create_engine("sqlite:///many2one_test.db")


# определяем модель для таблицы tevas
class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikas_id = Column(Integer, ForeignKey("vaikas.id"))
    vaikas = relationship("Vaikas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)


# создаем таблицы в базе данных
Base.metadata.create_all(engine)
