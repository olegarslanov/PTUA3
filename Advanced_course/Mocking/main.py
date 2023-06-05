# Mocking naudojamas:
# a) unittest veiktu automatiskai
# b) testuojant, kad nevyktu veiksmai su musu DB (sukuriamas fake DB)


# Pvz.:
from unittest.mock import patch

# cia reikia tureti faila "database.py" na kuri testuosime :)
from database import SqliteDatabase


@patch("database.SqliteDatabase.__init__")
def test_something(mock_init):
    # Здесь можно настроить поведение поддельного метода __init__ и проверить его вызовы
    mock_init.return_value = None  # Пример: замена возвращаемого значения
    mock_init.assert_called_once_with(
        ...
    )  # Пример: проверка вызова с определенными аргументами
    # Тестируемый код, использующий класс SqliteDatabase


# Продолжение кода тестов
