# Base class for all PyMongo exceptions. Here's an example of a Python code implementation using PyMongo, including handling the PyMongoError base exception. 
# The code demonstrates how to connect to a MongoDB database, perform a query, and handle potential exceptions:

from pymongo import MongoClient
from pymongo.errors import PyMongoError


def query_database() -> None:
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017")
        db = client["grocery_store"]
        collection = db["electronic"]

        # Perform a query
        result = collection.find_one({"name": "plaidie"})

        # Process the result
        if result:
            print("Found document:", result)
        else:
            print("Document not found.")

        # Close the MongoDB connection
        client.close()

    except PyMongoError as e:
        print("An error occurred:", str(e))


# Call the function
query_database()
