# Sukurti programą, kuri:
# Sukurtų duomenų bazę
# Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir
# ('Java', 'Tomas', 80)
# Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
# Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# Atspausdintų visas paskaitas (visą lentelę)


import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS
    paskaitos (
    pavadinimas text,
    destytojas text,
    trukme integer
    )"""
    )

    # Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir
    # ('Java', 'Tomas', 80)
    c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40)")
    c.execute("INSERT INTO paskaitos VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO paskaitos VALUES ('Java', 'Tomas', 80)")

    # Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
    c.execute("SELECT * From paskaitos WHERE trukme > 50")
    print(c.fetchall())

    # Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
    c.execute(
        "UPDATE paskaitos SET pavadinimas= 'Python programavimas' WHERE pavadinimas='Python'"
    )
    # Ištrintų paskaitą, kurios dėstytojas – „Tomas“
    c.execute("DELETE from paskaitos WHERE destytojas='Tomas'")

    # Atspausdintų visas paskaitas (visą lentelę)
    c.execute("SELECT * From paskaitos")
    print(c.fetchall())
