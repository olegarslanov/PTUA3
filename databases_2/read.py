from main import Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""


project1 = session.query(Project).get(4)  # ima eilute pagal id
print(project1.id)
print(project1.name)
print(project1.price)

project2 = (
    session.query(Project).filter_by(name="New Project 2").first()
)  # ima pirma rasta eilute su situ vardu
print(project2)

project3 = (
    session.query(Project).filter_by(name="New Project 1").all()
)  # all() naudojamas gauti visas eilutes su situ vardu
print(project3)

# project3 = (
#     session.query(Project).filter_by(name="New Project 1").one()
# )  # one() naudojamas gauti viena reiksme, jei nebus reiksmiu ar bus daugiau nei viena ismes klaida
# print(project3)
