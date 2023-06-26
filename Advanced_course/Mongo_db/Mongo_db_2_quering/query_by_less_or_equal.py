from typing import List
from pymongo import MongoClient

# Nurodau kur ieskoti
client = MongoClient("mongodb://localhost:27017")
db = client["grocery_store"]
collection = db["electronic"]


# Filtering using $lte operator (tai yra, kad reiksme butu mazesne ar lygi)
def filter_by_less_than_equal(
    field1: str, value1: int, field2: str, value2: float
) -> List[dict]:
    #  naudoju "$and" kad quering iskart kelias reiksmes
    query = {"$and": [{field1: {"$lte": value1}}, {field2: {"$lte": value2}}]}
    result = collection.find(query)
    return list(result)


# Example usage: Filter documents where the "quantity" field is <= 5 and price <= 20.00
filter_less_than_equal = filter_by_less_than_equal("quantity", 5, "price", 20.00)
print(filter_less_than_equal)
