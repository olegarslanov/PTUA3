# https://cataas.com/cat kas kartą užkrauna vis skirtingą katės nuotrauką.
# Parašykite funkciją, kuriai į parametrus įrašius, kiek norime nuotraukų, išsaugotų
# jas mūsų kompiuteryje.

import requests


def get_photoes(n):
    i = 0
    while i < n:
        r = requests.get("https://cataas.com/cat")
        with open(f"cat{i+1}.png", "wb") as f:
            f.write(r.content)
        i += 1


get_photoes(3)
