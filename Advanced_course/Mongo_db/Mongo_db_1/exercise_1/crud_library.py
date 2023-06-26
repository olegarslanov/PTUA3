# Create a class that would implement basic CRUD operations to manage book data in the library.

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import List, Dict, Any


class LibraryManager:
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

    def find_all_documents(self) -> List:
        documents = list(self.collection.find())
        return documents

    def find_document(self, document_id: str):
        document = self.collection.find_one({"_id": document_id})
        return document

    def update_document(self, document_id: str, updates: Dict) -> bool:
        result = self.collection.update_one({"_id": document_id}, {"$set": updates})
        return result.modified_count > 0

    def delete_document(self, document_id) -> bool:
        result = self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0


# Example usage

while True:
    choice = int(
        input(
            "Please enter Your choice: \n0 - conect to MongoDB \n1 - create document \n2 - read all documents \n3 - find document \n4 - update document \n5 - delete document \n6 - exit program \n"
        )
    )
    if choice == 0:
        # Connect to MongoDB ir tam tikros collection (sukuriam clases egzemplioriu)
        host = input("localhost:")
        port = int(input("27017:"))
        db_name = input("Books:")
        collection_name = input("science_books:")
        db = LibraryManager(host, port, db_name, collection_name)

    if choice == 1:
        # Create (Insert) document Operation
        document = {
            "name": "The 48 laws of power",
            "year": 45,
            "publisher": "Penguin's books",
            "author": "Robert Greene",
        }
        inserted_id = db.create_document(document)
        print(f"Inserted document with ID: {inserted_id}")

    if choice == 2:
        # Read all documents Operation
        document_id = {"name": "John Doe"}
        deleted_count = db.delete_document(document_id)
        print(f"Deleted {deleted_count} documents")

    # def delete_document(self, document_id) -> bool:
    #     result = self.collection.delete_one({"_id": document_id})
    #     return result.deleted_count > 0

    if choice == 5:
        # Delete document Operation
        document_id = {"name": "John Doe"}
        deleted_count = db.delete_document(document_id)
        print(f"Deleted {deleted_count} documents")

    if choice == 6:
        print("Exit program")
        exit()

    # def find_all_documents(self) -> List:
    #     documents = list(self.collection.find())
    #     return documents

    # def find_document(self, document_id: str):
    #     document = self.collection.find_one({"_id": document_id})
    #     return document
