# Create the CLI application, that would populate MongoDB database with random data. The input should ask for :

# *database name
# *collection name
# *field name with types (string, number, date string objects etc.) with range of values (lets say field name = price ,
# then value is number (float, int) which is random number from a(min) to b(max) )
# *number o documents to create.


from pymongo import MongoClient
from typing import List, Dict, Any, Optional
import random


class DatabaseManager:
    # connect to database
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    # create document
    def create_document(self, document: Dict) -> str:
        result = self.collection.insert_one(document)
        return str(result.inserted_id)


def populate_database():
    host = input("Please enter the MongoDB host (default: localhost): ") or "localhost"
    port = int(input("Please enter the MongoDB port (default: 27017): ") or 27017)
    db_name = input("Please enter the database name: ")
    collection_name = input("Please enter the collection name: ")
    field_name = input("Please enter the field name: ")
    field_type = input("Please enter the field type (string, number, date): ")
    min_value = float(input("Please enter the minimum value: "))
    max_value = float(input("Please enter the maximum value: "))
    doc_quant = int(input("Please enter the number of documents to create: "))

    document_manager = DatabaseManager(host, port, db_name, collection_name)


a = int(input("Please enter min number:"))
b = int(input("Please enter max number:"))
doc_quant = int(input("Please enter number of documents:"))

document = {
    "price": (random.randint(a, b)),
}

# kad pridaryti daugybe document

n = 0
while n <= doc_quant:
    document_manager.create_document(document)
    n += 1
