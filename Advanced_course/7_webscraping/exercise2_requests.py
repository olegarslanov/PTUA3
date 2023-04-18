# parašykite funkciją, kuri į args priimtų url eilučių sąrašą ir grąžintų, kokį serverį
# naudoja svetainė. Atsakymas galėtų atrodyti maždaug taip:

# URL                     Server
# -------------------------------------
# https://www.delfi.lt/   DWS
# https://www.alfa.lt/    nginx/1.10.3 (Ubuntu)
# https://www.15min.lt/   nginx
# https://www.lrytas.lt/  shield
# http://www.google.com/  gws


import requests

get_servers(
    "https://www.delfi.lt/",
    "https://www.alfa.lt/",
    "https://www.15min.lt/",
    "https://www.lrytas.lt/",
    "http://www.google.com/",
)


def get_servers(*urls):
    print("URL".ljust(30), "Server")
    print("-" * 40)
    for url in urls:
        response = requests.get(url)
        server = response.headers.get("Server")
        print(url.ljust(30), server)
