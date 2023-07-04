# Pasiimti anksčiau sukurtą programos kodą
# Funkcijas perdaryti taip, kad jos gražintų duomenis
# Sukurti UNIT testą visoms funkcijoms
# Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
# Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą


# 1. Gražinti trijų paduotų skaičių sumą.
def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


# 2. Gražintų paduoto sąrašo iš skaičių, sumą.
def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma


# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).


def didziausias_skaicius(*args):
    didziausias = args[0]
    for sk in args:
        if sk > didziausias:
            didziausias = sk
    return didziausias


# arba


def didziausias_skaicius2(*args):
    return max(args)


# 4. Gražintų paduotą stringą atbulai.
def stringas_atbulai(stringas):
    return stringas[::-1]


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
def info_apie_sakini(stringas):
    zodziu = len(stringas.split())
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    return f"Zodziu: {zodziu}, Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}"


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
def unikalus_sarasas(sarasas):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


# alternatyva:


def unique_only(*args):
    return list(set(args))


# print(unique_only(4, 5, "Labas", 6, "Labas", True, 5, True, 10))


# 7. Gražintų, ar paduotas skaičius yra pirminis.

# n = int(input("Įveskite skaičių "))


def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return False
        return True
    return False


# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo


def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return " ".join(zodziai)


# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.

import calendar


def ar_keliamieji(metai):
    return calendar.isleap(metai)


# 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

import datetime


def patikrinti_data(sukaktis):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
    now = datetime.datetime.now()
    skirtumas = now - ivesta_data
    return ("Praėjo metų: ", skirtumas.days // 365)
    # print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
    # print("Praėjo savaičių: ", skirtumas.days // 7)
    # print("Praėjo dienų: ", skirtumas.days)
    # print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
    # print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
    # print("Praėjo sekundžių: ", skirtumas.total_seconds())


# patikrinti_data("2000-01-01 12:12:12")
# patikrinti_data("1991-03-11 12:12:12")
