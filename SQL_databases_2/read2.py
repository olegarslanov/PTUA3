from main import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""


# Kaip ieškoti duomenų pagal sąlygą ar šabloną:

# search = session.query(Project).filter(Project.name.ilike("2%"))
search2 = session.query(Project).filter(Project.price > 1000)
# search3 = session.query(Project).filter(Project.price > 1000, Project.name.ilike("2%"))

# print([i for i in search])
print([i for i in search2])
# print([i for i in search3])
