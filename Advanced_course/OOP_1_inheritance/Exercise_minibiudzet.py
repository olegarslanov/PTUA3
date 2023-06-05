# Padaryti minibiudžeto programą, kuri:
# Leistų vartotojui įvesti pajamas
# Leistų vartotojui įvesti išlaidas
# Leistų vartotojui parodyti pajamų/išlaidų balansą
# Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# Leistų vartotojui išeiti iš programos

from typing import List


class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma


class Biudzetas:
    def __init__(self) -> None:
        self.zurnalas: List = []

    def prideti_pajamu(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    def irasyti_islaidas(self, suma):
        islaidos = Irasas("Islaidos", suma)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            else:
                suma -= irasas.suma
        return suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(f"{irasas.tipas}: {irasas.suma}")


biudzet = Biudzetas()

while True:
    print(
        "Pasirinkite: \n1 - Prideti pajamas, \n2 - Irasyti islaidas, \n3 - Gauti balansa, \n4 - Parodyti ataskaita, \n5 - Exit"
    )

    choice = int(input("Please enter Your choice: "))

    if choice == 1:
        suma = float(input("Iveskite pajamu suma: "))
        biudzet.prideti_pajamu(suma)
    elif choice == 2:
        biudzet.irasyti_islaidas(float(input("Iveskite islaidu suma: ")))
    elif choice == 3:
        print(biudzet.gauti_balansa())
    elif choice == 4:
        biudzet.parodyti_ataskaita()
    elif choice == 5:
        break
