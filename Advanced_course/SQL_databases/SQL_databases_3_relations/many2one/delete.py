from models import Vaikas, Tevas
from session import session


tevas = session.query(Tevas).get(2)
session.delete(tevas)
session.commit()
