from bs4 import BeautifulSoup
import requests


# Jei noriu gauti visa puslapio koda:
source = requests.get("https://www.delfi.lt/").text

soup = BeautifulSoup(source, "html.parser")
# Galiu atprintinti visa saita
# print(soup.prettify())
# gaunu elementa div su klase "elements" (kurioje yra man reikalingu duomenu)
blokas = soup.find("div", class_="elements")
# print(blokas.prettify())
# gaunu visus tegus "a"
tekstas = blokas.find_all("a")
# isimu reikalinga 4 tega ir su text.strip() pasalinu nereikalinga teksta is abieju pusiu
link = tekstas[3].text.strip()
print(link)
# gaunu atributo href reiksme
print(tekstas[3]["href"])
