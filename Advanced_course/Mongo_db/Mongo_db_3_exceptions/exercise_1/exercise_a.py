# Using all Exceptions explained above, create a simple application(s) to test (if possible in local environment)
# all of them. Use Docker Container for live connection.


from pymongo import MongoClient
from pymongo.errors import PyMongoError, OperationFailure, ConnectionFailure


def connect_to_mongodb():
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhst:27017/")
        db = client["mydatabase"]
        collection = db["mycollection"]
        return collection
    
    except ConnectionFailure as e:
        raise Exception("Failed to connect to server:", str(e))
    
    
    except OperationFailure as e:
        raise Exception("Failed to connect to MongoDB:", str(e))


    except PyMongoError as e:
        raise Exception("Failed to connect:", str(e))

# Usage
def main():
    try:
        collection = connect_to_mongodb()
        document1 = {"id": 1, "age": 30}
        result1 = collection.insert_one(document1)
        print("Connected to MongoDB successfully. Document ID:", result1.inserted_id)
     
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()


