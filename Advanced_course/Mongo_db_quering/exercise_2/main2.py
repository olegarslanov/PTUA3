# Write a function filter_documents that takes a MongoDB collection, a field name,
# an equal value, and a not equal value as parameters. The function should return a
# list of documents from the collection where the specified field is equal to the equal
# value and not equal to the not equal value.


from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection


def filter_documents(
    collection: Collection, field_name: str, eq_value: str, ne_value: str
) -> List[dict]:
    """
    Filters documents in a MongoDB collection based on field values using $eq and $ne operators.

    Args:
        collection: The MongoDB collection to filter.
        field_name: The name of the field to filter.
        eq_value: The equal value to match.
        ne_value: The not equal value to exclude.

    Returns:
        A list of documents that match the filter criteria.
    """
    query = {field_name: {"$eq": eq_value, "$ne": ne_value}}
    result = collection.find(query)
    return list(result)
