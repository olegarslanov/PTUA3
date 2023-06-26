# With your own tool, create of database of grocery store. Store consist three different categories of items
#  (lets say electronics, fruits, food etc.). The items as minimum should have these fields: name, price, 
# quantity, year made (YYYY-MM-DD).
# Get all electronic items monetary value made 1 years, 2 months and 12 days from today.
# Get average price for all items/categories in the store.
# Get all items which names starts with letter a, and cost is between 10 and 100.
# Find all item names (only) for prices > 50 and quantity < 10.


from pymongo import MongoClient
from typing import Dict
import random
import datetime


class DatabaseManager:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_document(self, document: Dict) -> str:
        result = self.collection.insert_one(document)
        return str(result.inserted_id)


# Usage:
def populate_database():
    host = input("Please enter the MongoDB host (default: localhost): ") or "localhost"
    port = int(input("Please enter the MongoDB port (default: 27017): ") or 27017)
    db_name = input("Please enter the database name: ")
    collection_name = input("Please enter the collection name: ")
    doc_quant = int(input("Please enter the number of documents to create: "))
    field_quant = int(input("Please enter the number of fields in document:"))

    document_manager = DatabaseManager(host, port, db_name, collection_name)


    for _ in range(doc_quant):
        document = {}
        for _ in range(field_quant):
            field_name = input("Please enter the field name: ")
            field_type = input("Please enter the field type (string, number, date): ")
           
            if field_type == "string":
                value = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
            elif field_type == "number":
                min_value = float(input("Please enter the minimum value: "))
                max_value = float(input("Please enter the maximum value: "))
                value = random.uniform(min_value, max_value)
            elif field_type == "date":
                value = random_date()
            else:
                value = None

            document[field_name] = value

        document_manager.create_document(document)

    print("Database population completed.")

def random_date(start_date="2020-01-01", end_date="2023-12-31"):
    start_datetime = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    days_difference = (end_datetime - start_datetime).days
    random_days = random.randint(0, days_difference)
    random_date = start_datetime + datetime.timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    populate_database()

