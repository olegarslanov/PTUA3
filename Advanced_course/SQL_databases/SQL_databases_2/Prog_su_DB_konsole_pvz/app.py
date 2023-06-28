# Sukuriam ryšį su sukurta DB (main.py) is sio failo:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import engine, Project

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

# Prasideda interface:
while True:
    pasirinkimas = int(
        input(
            "Pasirinkite veiksmą: \n1 - atvaizduoti projektus \n2 - sukurti projektą \n3 - pakeisti projektą \n4 - ištrinti projektą \n5 - iseiti is programos \n"
        )
    )

    if pasirinkimas == 1:
        projektai = session.query(Project).all()
        print("-------------------")
        for project in projektai:
            print(project)
        print("-------------------")

    if pasirinkimas == 2:
        name = input("Įveskite projekto pavadinimą")
        price = float(input("Įveskite projekto kainą"))
        project = Project(name, price)
        session.add(project)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Project).all()
        print("-------------------")
        for project in projektai:
            print(project)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID"))
        keiciamas_project = session.query(Project).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - pavadinimą, 2 - kainą"))
        if pakeitimas == 1:
            keiciamas_project.name = input("Įveskite projekto pavadinimą")
        if pakeitimas == 2:
            keiciamas_project.price = float(input("Įveskite projekto kainą"))
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Project).all()
        print("-------------------")
        for project in projektai:
            print(project)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo ištrinti projekto ID"))
        trinamas_project = session.query(Project).get(keiciamo_id)
        session.delete(trinamas_project)
        session.commit()

    if pasirinkimas == 5:
        print("Exit program")
        break


# Paaiskinimas:
# Этот код на Python использует библиотеку SQLAlchemy и модуль "main" для создания интерфейса
# командной строки для управления базой данных SQLite и таблицей "Projektas".

# Сначала создается объект "engine" класса "create_engine", который создает соединение с базой
# данных SQLite и указывает путь к файлу базы данных.

# Далее создается объект "Session" класса "sessionmaker", который используется для создания
# сессии базы данных. Сессия представляет собой интерфейс для взаимодействия с базой данных.

# Затем создается бесконечный цикл, который предлагает пользователю выбрать действие из четырех
# вариантов:

# Вывести список проектов.
# Создать новый проект.
# Изменить проект.
# Удалить проект.
# Если пользователь выбирает "1", то выполняется запрос к базе данных, чтобы получить список
# всех проектов. Затем все проекты выводятся на экран.

# Если пользователь выбирает "2", то запрашивается название и цена нового проекта, затем
# создается новый объект класса "Project" и добавляется в базу данных.

# Если пользователь выбирает "3", то выполняется запрос к базе данных, чтобы получить список
# всех проектов. Затем пользователю предлагается выбрать ID проекта, который нужно изменить.
# Затем пользователю предлагается выбрать, какое значение проекта нужно изменить (название или
# цену), и вводится новое значение.

# Если пользователь выбирает "4", то выполняется запрос к базе данных, чтобы получить список
# всех проектов. Затем пользователю предлагается выбрать ID проекта, который нужно удалить, и
# проект удаляется из базы данных.

# В конце каждой операции выполняется команда "session.commit()", чтобы сохранить изменения в
# базе данных.
