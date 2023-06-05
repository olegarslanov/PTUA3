# Write a function filter_documents that takes a MongoDB collection, a field name,
# an equal value, and a not equal value as parameters. The function should return a
# list of documents from the collection where the specified field is equal to the equal
# value and not equal to the not equal value.


from pymongo import MongoClient
from typing import List


client = MongoClient("mongodb://localhost:27017/")
db = client["testdb"]
collection = db["collection5"]


def filter_documents3(field_name, equal_value, not_equal_value):
    query = {field_name: {"$ne": not_equal_value}}
    result_not_eq = collection.find(query)
    query = {field_name: {"$eq": equal_value}}
    result_eq = collection.find(query)
    print(list(result_eq))
    print(list(result_not_eq))


filter_documents3("age", 30, 30)
