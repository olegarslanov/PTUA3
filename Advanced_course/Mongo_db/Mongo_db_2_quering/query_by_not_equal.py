from typing import List
from pymongo import MongoClient

# Nurodau kur ieskoti
client = MongoClient("mongodb://localhost:27017")
db = client["grocery_store"]
collection = db["electronic"]


# Filtering using $nin operator (tai yra, kad reiksmes neatitiktu butens situ reiksmiu)
def filter_by_nin(field_name: str, values: List[int]) -> List[dict]:
    query = {field_name: {"$nin": values}}
    result = collection.find(query)
    return list(result)


# Example usage: Filter documents where the "quantity" field is = 10
filter_by_nin_10 = filter_by_nin("quantity", [5, 10, 15])
print(filter_by_nin_10)
