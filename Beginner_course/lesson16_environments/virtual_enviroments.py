# Pipenv /////

# Pipenv yra trečiosios šalies paketas, todėl pirmiausia jį reikia įdiegti:
# pip install pipenv

# Tada galite pereiti į savo produkto katalogą (arba sukurti naują katalogą, jei pradedate naują projektą, kaip čia darau aš) ir jame įdiegti ipipenv:
# mkdir ~/dev/projects/my-new-project && cd ~/dev/projects/my-new-project
# pipenv install

# Taip bus sukurti du nauji failai: Pipfile ir Pipfile.lock.

# Norėdami įjungti virtualią aplinką:
# $ pipenv shell

# Norėdami įdiegti paketus su ipenv:
# pipenv install <paketo pavadinimas>

# Paketų įtraukimas į aplinką:
# pipenv lock

# Norėdami parodyti, kokie paketai yra įdiegti (ir jų priklausomybės), galite paleisti:
# pipenv graph

# Paketų pašalinimas:
# pipenv uninstall <paketo pavadinimas>


# Venv ////

# Sukurti virtualia aplinka:
# python -m venv .venv

# Aktyvuoti virt. aplinka:
# source .venv/Scripts/activate

# Kad istaliuoti paketus/bibliotekas:
# pip install <paketo pavadinimas>

# Deaktyvuoti virt. a.:
# deactivate

# Perziureti kokie paketai instaliuoti:
# pip freeze

# Sugeneruoti automatiskai requirements.txt: (nurodo siame faile kokiu bibliotekos versiju reikia, kad korektiskai veiktu programa)
# pip freeze > requirements.txt

# Greitai instaliuoti virt. aplink. tas pacias biblioteku versijas:
# pip install -r requirement.txt

# Greitai deinstaliuoti virt. aplink. visas bibliotekas:
# pip uninstall -r requirement.txt -y


# Kaip suprasti kad esu virt. aplinkoje:
# terminalo eiluteje turi buti uzrasas ".venv"
