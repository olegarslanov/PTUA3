# Connect to a MongoDB server running on localhost.
# Create a new database named 'exercise_db' and a collection named 'exercise_collection'.
# Define the following JSON schema validation rules for the collection:
# The document must be an object.
# The 'name' field is required and must be a string.
# The 'age' field is required and must be an integer between 18 and 99.
# The 'email' field is required and must be a string containing a valid email address.
# Insert three documents into the collection, one that satisfies the validation rules and two that violate the validation rules.
# Print all the documents in the collection.
# Clean up by dropping the collection and closing the MongoDB connection.


from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import OperationFailure, PyMongoError


validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "age", "email"],
            "properties": {
                "name": {"bsonType": "string"},
                "age": {
                    "bsonType": "int",
                    "minimum": 18,
                    "maximum": 99,
                },
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                },
            },
        }
    }
}


# Connect to MongoDB
class Database:
    def __init__(self, db_name: str, collection: Collection):
        self.client: MongoClient = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection]


database = Database(db_name="exercise_db", collection="exercise_collection")

# Idedamas tuscias document, kad automatiskai susikurtu collection. Kitaip ismetinetines klaida, kadangi is pradziu dar nesukurta collection db buna (o eina validation_rules)
database.collection.insert_one({})

try:
    database.db.command("collMod", database.collection.name, validator=validation_rules)
    print("Schema validation enabled.")
except OperationFailure as e:
    print(f"Failed to enable schema validation: {e.details['errmsg']}")


# Validate and insert documents into the collection
valid_doc = {"name": "John Doe", "age": 80, "email": "johndoe@example.com"}
invalid_doc1 = {"name": "Invalid1", "age": 17, "email": "invalid1@example.com"}
invalid_doc2 = {"name": "Invalid2", "age": 19, "email": "invalid2@example.com"}

database.collection.insert_one(valid_doc)
database.collection.insert_one(invalid_doc1)
database.collection.insert_one(invalid_doc2)

# except PyMongoError as e:
#     print(f"Failed to insert document: {e}")


# Print all documents from the collection
documents = database.collection.find()
for doc in documents:
    print(doc)

# Clean up
database.collection.drop()
database.client.close()


# invalid_doc2 = {"name": "Invalida2", "age": 10, "email": "invalidas@example.cm"}
# try:
#     collection.insert_one(invalid_doc2)
#     print("Yes of course. Document in db")
# except Exception as e:
#     print(f"Failed to insert document: {e}")
