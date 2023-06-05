from pymongo import MongoClient
from typing import List, Dict, Any, Optional

document_one = {
    "document_name": "Samata",
    "description": "Namo dezute",
    "plot_in_m2": 140,
    "adress": "Kaunas",
    "budget": 115000,
    "estimate_price": 370,
    "estimator_name": "Tomas",
    "preparation_termin_in_days": 14,
    "project_author": "Klevas",
    "estimate_date": "2023-04-12",
}


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

    def get_single_query(
        self, query: Dict[str, Any], fields: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        return self.collection.find_one(query, fields)


document_manager = LibraryManager(
    host="localhost", port=27017, db_name="tasksdb", collection_name="queries"
)

# kad pridaryti daugybe document
# print(document_manager.create_document(document_one))

# Filtruoju pagal tam tikra parametra ("budget":100000), bei nurodau tik tam tikrus document laukus(jeigu pasirinksiu 0 tai tada tos laukus neparodys, jei 1 parodys)
query = {"budget": 100000}
fields = {"document_name": 1, "budget": 1}
document = document_manager.get_single_query(query, fields)
print(document)
