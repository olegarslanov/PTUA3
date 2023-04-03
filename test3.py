import argparse

# Создание парсера аргументов
parser = argparse.ArgumentParser(description="Описание скрипта")

# Добавление опций
parser.add_argument("-r", "--reserved", type=int, help="Зарезервированный номер стола")

# Парсинг аргументов
args = parser.parse_args(3)

# Использование аргументов
if args.reserved:
    print("Зарезервированный номер стола:", args.reserved)
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    time_reserved = input("Введите время бронирования: ")
    print(
        "Имя: {}\nФамилия: {}\nВремя бронирования: {}".format(
            name, surname, time_reserved
        )
    )
    # здесь можно добавить код для обработки имени, фамилии и времени зарезервированного столика
else:
    print("Номер зарезервированного стола не был указан")
    # здесь можно добавить код для обработки отсутствия зарезервированного столика
