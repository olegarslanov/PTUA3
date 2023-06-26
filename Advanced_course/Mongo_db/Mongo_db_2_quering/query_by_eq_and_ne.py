from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://localhost:27017")
db = client["grocery_store"]
collection = db["electronic"]


def filter_by_eq_and_ne(
    collection: Collection, field_name: str, equal_value: int, not_equal_value
) -> List[dict]:
    query = {field_name: {"$eq": equal_value, "$ne": not_equal_value}}
    result = collection.find(query)
    return list(result)


print(filter_by_eq_and_ne(collection, "quantity", 19, 29))
