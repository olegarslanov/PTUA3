from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

def insert_document(collection, document):
    try:
        collection.insert_one(document)
        print("Документ успешно вставлен.")
    except DuplicateKeyError as e:
        print("Произошла ошибка дублирования ключа:", str(e))

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase1"]
collection = db["mycollection"]

# Документ для вставки
document1 = {"_id": 1, "name": "John"}
document2 = {"_id": 1, "name": "Alice"}

# Вставка первого документа
insert_document(collection, document1)

# Вставка второго документа (с дублирующимся ключом)
insert_document(collection, document2)
