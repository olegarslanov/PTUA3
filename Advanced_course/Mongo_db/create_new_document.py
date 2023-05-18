from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)


# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "Books"
    collection_name = "science_books"

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Create (Insert) Operation
    document = {
        "name": "The 48 laws of power",
        "year": 40,
        "publisher": "Penguin books",
        "author": "Robert Greene",
    }
    inserted_id = insert_document(collection, document)
    print(f"Inserted document with ID: {inserted_id}")
