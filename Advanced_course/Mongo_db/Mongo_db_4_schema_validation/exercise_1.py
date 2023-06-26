# Konvertuoti i validation rules as a dictionary (kad galetume naudoti nustatant kas ieis i musu DB)


# json object

json_object = {
    "name": "John Doe",
    "age": 25,
    "is_student": True,
    "interests": ["reading", "traveling", "photography"],
    "address": {
        "street": "123 Main Street",
        "city": "New York",
        "country": {"name": "United States", "code": "US"},
    },
    "birth_date": "1998-05-10",
    "metadata": {"category": "A", "priority": 1},
    "favorite_things": ["apple", 5, False],
}

# Define the validation rules as a dictionary

validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "name",
                "age",
                "is_student",
                "interests",
                "address",
                "birth_date",
                "metadata",
                "favorite_things",
            ],
            "properties": {
                "name": {"bsonType": "string"},
                "age": {"bsontype": "int"},
                "is_student": {"bsonType": "bool"},
                "interests": {"bsonType": "array"},
                "address": {
                    "bsonType": "object",
                    "required": ["street", "city", "country"],
                    "properties": {
                        "street": {"bsonType": "string"},
                        "city": {"bsonType": "string"},
                        "country": {
                            "bsonType": "object",
                            "required": ["name", "code"],
                            "properties": {
                                "name": {"bsonType": "string"},
                                "code": {"bsonType": "string"},
                            },
                        },
                    },
                },
                "birth_date": {"bsonType": "date"},
                "metadata": {
                    "bsonType": "object",
                    "required": ["category", "priority"],
                    "properties": {
                        "category": "string",
                        "priority": "int",
                    },
                },
                "favorite_things": {"bsonType": "array"},
            },
        }
    }
}
