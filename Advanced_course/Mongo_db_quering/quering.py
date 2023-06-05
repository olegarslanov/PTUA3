# We can query a MongoDB database using PyMongo with the find function to get all the results 
# satisfying the given condition and also using the find_one function, which will return only 
# one result satisfying the condition.

# The following is the syntax of the find and find_one:

your_collection.find( {<< query >>} , { << fields>>} )


# Filter based on fields & conditions ////

# For instance, you have hundreds of fields and you want to see only a few of them. You can
# do that by just putting all the required field names with the value 1. For example:
# (jeigu :1 tada rodom dokumento nurodytus laukus, jei :0 tai visus rodom o nurodytus nerodome)

your_shop_collection.find_one({}, {"week": 1, "checkout_price": 1})
your_shop_collection.find_one({}, {"num_orders": 0, "meal_id": 0})

# Now, in this section, we will provide a condition in the first braces and fields to discard
# in the second. Consequently, it will return the first document with center_id equal to 55
# and meal_id equal to 1885 and will also discard the fields _id and week:
# (iskart dict nurodau kokius parametru parodyti documentus, kitame dict nurodau kad nerodyti document tam tikrus laukus)

your_shop_collection.find_one({"center_id": 55, "meal_id": 1885}, {"_id": 0, "week": 0})


# Filter based on Comparison Operators ////

NAME	DESCRIPTION
# lygu, nelygu
$eq	    It will match the values that are equal to a specified value.
$ne	    It will match all the values that are not equal to a specified value.
# daugiau, maziau
$gt	    It will match the values that are greater than a specified value.
$lt	    It will match all the values that are less than a specified value.

$gte	It will match all the values that are greater than or equal to a specified value.
$in	    It will match any of the values specified in an array.
$lte	It will match all the values that are less than or equal to a specified value.
$nin	It will match none of the values specified in an array.



$gt и $lt
Вот примеры кода для фильтрации с MongoDBиспользованием операторов (больше) и (меньше):PyMongo$gt$lt

from typing import List
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Filtering using $gt operator
def filter_by_greater_than(field_name: str, value: int) -> List[dict]:
    query = {field_name: {"$gt": value}}
    result = collection.find(query)
    return list(result)

# Example usage: Filter documents where the "age" field is greater than 25
filtered_greater_than = filter_by_greater_than("age", 25)
print(filtered_greater_than)


# Filtering using $lt operator
def filter_by_less_than(field_name: str, value: int) -> List[dict]:
    query = {field_name: {"$lt": value}}
    result = collection.find(query)
    return list(result)

# Example usage: Filter documents where the "rating" field is less than 4.5
filtered_less_than = filter_by_less_than("rating", 4.5)
print(filtered_less_than)
