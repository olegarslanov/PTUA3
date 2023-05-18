from models import Vaikas, Tevas
from session import session


tevas = session.query(Tevas).get(2)
vaikas1 = tevas.vaikai[0]
tevas.vaikai.remove(vaikas1)  # ismetam realiation motinos su vaikas1
session.commit()
