from models import Vaikas, Tevas
from session import session

vaikas = session.query(Vaikas).get(1)

for tevas in vaikas.tevai:
    print(tevas.vardas)

tevas1 = session.query(Tevas).get(1)

print(tevas.vaikas.vardas)
