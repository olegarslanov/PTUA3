from main import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""


project1 = Project("New Project 1", 20000)
session.add(project1)
session.commit()

project2 = Project("New Project 2", 55000)
session.add(project2)
session.commit()
