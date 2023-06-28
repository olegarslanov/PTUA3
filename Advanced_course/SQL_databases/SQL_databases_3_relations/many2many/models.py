from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# создаем подключение к базе данных
engine = create_engine("sqlite:///many2many_test.db")

# создаем экземпляр класса declarative_base
Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("tevas_id", Integer, ForeignKey("tevas.id")),
    Column("vaikas_id", Integer, ForeignKey("vaikas.id")),
)


# определяем модель для таблицы tevas
class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikai = relationship("Vaikas", secondary=association_table, back_populates="tevai")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    tevai = relationship("Tevas", secondary=association_table, back_populates="vaikai")


# создаем таблицы в базе данных (no tolko vyzyvaetsja iz etogo faila iz drugih ne prohodit)
if __name__ == "__main__":
    Base.metadata.create_all(engine)
