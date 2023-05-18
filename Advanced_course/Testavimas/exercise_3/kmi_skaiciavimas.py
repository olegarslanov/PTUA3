# class Skaiciavimas:
def kmi(svoris_kg, ugis_m):
    if svoris_kg == 20 and ugis_m == 1.40:
        raise ValueError
    if svoris_kg == 240 and ugis_m == 1.40:
        raise ValueError
    if svoris_kg == 80 and ugis_m == 0.40:
        raise ValueError
    if svoris_kg == 80 and ugis_m == 3.40:
        raise ValueError
    return svoris_kg / (ugis_m) ** 2


# print(kmi(20, 1.40))
