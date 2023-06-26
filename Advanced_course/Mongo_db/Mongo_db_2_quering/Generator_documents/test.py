# from pymongo import MongoClient
# from typing import Dict
# import random
# import pandas as pd


# document = {}
# for _ in range(2):
#     field_name = input("Please enter the field name: ")
#     field_type = input("Please enter the field type (string, number, date): ")
#     if field_type == "string":
#         value = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
#     else:
#         value = None

#     document[field_name] = value

# print(document)


from pymongo import MongoClient
from typing import Dict
import random
import pandas as pd


document = {}
for _ in range(2):
    field_name = input("Please enter the field name: ")
    field_type = input("Please enter the field type (string, number, date): ")
    if field_type == "string":
        value = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))
    else:
        value = None

    document[field_name] = value

print(document)
