# Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų ir atspausdintų
# oro prognozę Vilniuje šiuo metu. Galima naudoti str metodus, regex.

import requests
import re


url = "https://orai.15min.lt/prognozes"
response = requests.get(url)

vilnius_regex = r'<div class="place forecast selected" data-place="vilnius">\s*<span class="place-name">\s*Vilnius\s*</span>\s*<div class="temp">\s*([^<]+)\s*</div>'
weather_text = re.search(vilnius_regex, response.text).group(1)


print(f"Vilnius: {weather_text}")
