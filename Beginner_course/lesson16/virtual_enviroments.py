

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






import numpy as np
import pandas as pd


print(np.sin(1))
print(pd.value_counts("humpy as eee"))
