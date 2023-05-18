# Sukurti programą, kuri:
# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą,
# nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).

# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

from sqlalchemy import create_engine
from main import engine, Projektas
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///projektas_exercise1.db")
Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

while True:
    pasirinkimas = int(
        input(
            "Pasirinkite veiksmą: \n1 - atvaizduoti darbuotojus \n2 - irasyti darbuotoja \n3 - atnaujinti darbuotoja \n4 - ištrinti darbuotoja \n5 - iseiti is programos"
        )
    )

    if pasirinkimas == 1:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")

    if pasirinkimas == 2:
        while True:
            try:
                name = input("Iveskite varda:")
                surname = input("Iveskite pavarde:")
                born_date = input("Iveskite gimimo data:")
                position = input("Iveskite pareigas:")
                salary = float(input("Iveskite alyginima:"))

                projektas = Projektas(name, surname, born_date, position, salary)
                session.add(projektas)
                session.commit()
                break
            except:
                print("Kazkas negerai. Patikrinkite ivedamus duomenys")

    if pasirinkimas == 3:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")

        keiciamo_id = int(input("Pasirinkite norimo pakeisti darbuotojo id:"))
        keiciamas_darbuotojas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(
            input(
                "Ką norite pakeisti: 1 - varda, 2 - pavarde, 3 - gimimo data, 4 - pareigas, 5 - atlyginima :"
            )
        )
        if pakeitimas == 1:
            keiciamas_darbuotojas.name = input("Įveskite darbuotojo varda:")
        if pakeitimas == 2:
            keiciamas_darbuotojas.surname = input("Įveskite darbuotojo pavarde:")
        if pakeitimas == 3:
            keiciamas_darbuotojas.born_date = input("Įveskite darbuotojo gimimo data:")
        if pakeitimas == 4:
            keiciamas_darbuotojas.position = input("Įveskite darbuotojo pareigas:")
        if pakeitimas == 5:
            keiciamas_darbuotojas.salary = float(
                input("Įveskite darbuotojo atlyginima:")
            )
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Projektas).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo ištrinti darbuotojo id:"))
        trinamas_darbuotojas = session.query(Projektas).get(keiciamo_id)
        session.delete(trinamas_darbuotojas)
        session.commit()

    if pasirinkimas == 5:
        print("Iki")
        break
