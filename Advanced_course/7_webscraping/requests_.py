import requests

#        Galiu nukopinti visa puslapio koda (.text grazina puslapio turini numatytuoju formatu
# (siuo atveju HTML), .content metodas grazina turini binary formatu)
response = requests.get("http://google.com")
print(response.text)
print(rrsponse.content)

#        Galiu paziureti, bei issaugoti paveiksleli i python faila
r = requests.get("https://www.python.org/static/img/python-logo.png")
print(r.content)
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01"\x00\x00\x00R\x08\x06\x00\x00\x00\xf0\xeb\xd9\xc3\x00\x00\x00\tpHYs\x00\x00\x0b\x13......

with open("logo.png", "wb") as f:
    f.write(r.content)

#       Galiu patikrinti ar prisijungiau, ar ne:
r = requests.get("http://python.org/blabla")
if r.status_code not in range(400, 600):
    print("Pavyko prisijungti! Dirbame toliau...")
else:
    print(f"Kažkas ne taip.. Kodas {r.status_code}")
# # Kažkas ne taip.. Kodas 404

# Jei noriu gauti visa puslapio koda:
r = requests.get("https://www.python.org/search/?q=pep")
print(r.text)

# Kai mes kazka kazkur postinam
data = {"name": "Jonas", "lastname": "Jonaitis"}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
# ...
# "form": {
#     "lastname": "Jonaitis",
#     "name": "Jonas"
#   },
#  ...


#       Pabandziau pazaisti www.httpbin.org:
# Image
# download image
r = requests.get("https://www.httpbin.org/image/webp")
# print(r.content)
with open("wolf_head3.png", "wb") as f:
    f.write(r.content)

# gaunu header'ius
r = requests.get("https://www.httpbin.org/image/webp")
print(r.headers)

# gaunu requests koda
r = requests.get("https://www.httpbin.org/image/webp")
print(r.status_code)
# 200

# gaunu IP
r = requests.get("https://www.httpbin.org/ip")
print(r.text)
# "origin": "88.223.204.98"
