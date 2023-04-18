# Sukurti programą, kuri:

# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
# Atspausdintų tekstą iš sukurto failo
# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# Atspausdintų visą failo tekstą atbulai
# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
# Patarimai:

# Naudoti from datetime import datetime, datetime.today()
# Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
# Kai kur galima panaudoti funkcijas iš praeitų pamokų

import datetime


zen = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

while True:
    veiksmas = int(
        input(
            "Pasirinkite veiksmą: 1 - sukurti faila 'Tekstas.txt', 2 - Atspausdintų tekstą iš sukurto failo, 3 - Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką, 4 - Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių), 5 - Sukurtame faile eilutę 'Beautiful is better than ugly.', 6 - pakeistų į 'Gražu yra geriau nei bjauru.', 7 - Atspausdintų visą failo tekstą atbulai, 8 - Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių, 9 - Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS"
        )
    )

    if veiksmas == 1:
        with open("Tekstas.txt", "w") as f:
            f.write(zen)
            break

    if veiksmas == 2:
        with open("Tekstas.txt", "r") as f:
            print(f.read())
            break

    if veiksmas == 3:
        with open("Tekstas.txt", "a") as f:
            a = datetime.datetime.now()
            f.write(str(a))
            break
    if veiksmas == 4:
            with open("Tekstas.txt", "r") as f:
            for eilute in f:
                f.write(eilute += 1, end=" ")
                break
