from main import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

project1 = session.query(Project).filter_by(name="New Project 1").one()

session.delete(project1)
session.commit()
