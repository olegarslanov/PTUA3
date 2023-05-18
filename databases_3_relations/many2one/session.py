from sqlalchemy.orm import sessionmaker
from models import engine

# создаем экземпляр класса Session
Session = sessionmaker(bind=engine)
session = Session()
