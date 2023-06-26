from typing import List
from pymongo import MongoClient

# Nurodau kur ieskoti
client = MongoClient("mongodb://localhost:27017")
db = client["grocery_store"]
collection = db["electronic"]


# Filtering using $in operator (tai yra kad reiksmes atitiktu butens sita reiksme)
def filter_by_in(field_name: str, values: List[int]) -> List[dict]:
    query = {field_name: {"$in": values}}
    result = collection.find(query)
    return list(result)


# Example usage: Filter documents where the "quantity" field is = 10
filter_by_in_5 = filter_by_in("quantity", [5])
filter_by_in_10 = filter_by_in("quantity", [10])
filter_by_in_15 = filter_by_in("quantity", [15])
print(filter_by_in_5)
print(filter_by_in_10)
print(filter_by_in_15)
