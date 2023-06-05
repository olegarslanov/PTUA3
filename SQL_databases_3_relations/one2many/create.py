from models import Vaikas, Tevas
from session import session


vaikas = Vaikas(vardas="Vaikas", pavarde="Vaikaitis")
vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")

tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")

tevas.vaikai.append(vaikas)  # per cia as prisegu vaikas prie tevo
tevas.vaikai.append(vaikas2)
# object.atribute.method(object)
# per cia as prisegu vaikas2 prie tevo (modulyje "models" class "Tevas" yra atributas "vaikai", kuris sukuria sita rysi)

session.add(tevas)
session.commit()


# Этот фрагмент кода использует SQLAlchemy для создания и хранения объектов, представляющих
# людей (отца и его детей) в базе данных. Вот шаги, которые он выполняет:

# Он импортирует объект session из модуля session. Этот объект используется для
# взаимодействия с базой данных.

# Он создает два объекта Vaikas (представляющих детей) и один объект Tevas
# (представляющий отца) с использованием соответствующих классов.

# Он добавляет два объекта Vaikas в качестве детей к объекту Tevas, используя метод
# append() атрибута vaikai объекта Tevas.

# Он добавляет объект Tevas в сессию, используя метод add() объекта session.

# Он фиксирует изменения в базе данных с использованием метода commit() объекта session.

# Этот код в основном создает родительско-детскую связь в базе данных между объектом
# Tevas и двумя объектами Vaikas, используя атрибут vaikai объекта Tevas в качестве
# списка для хранения ссылок на его детей.
