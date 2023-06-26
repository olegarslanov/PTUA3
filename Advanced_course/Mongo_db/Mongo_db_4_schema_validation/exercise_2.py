# Konvertuoti i validation rules as a dictionary (kad galetume naudoti nustatant kas ieis i musu DB)

json_object = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "address": {
            "street": "456 Elm Street",
            "city": "San Francisco",
            "country": {"name": "United States", "code": "US"},
        },
        "contacts": [
            {"type": "email", "value": "john.doe@example.com"},
            {"type": "phone", "value": "1 123-456-7890"},
        ],
        "education": [
            {
                "institution": "University of XYZ",
                "degree": "Bachelor's",
                "major": "Computer Science",
                "completed": True,
            },
            {
                "institution": "ABC College",
                "degree": "Master's",
                "major": "Data Science",
                "completed": False,
            },
        ],
    },
    "products": [
        {"id": 1, "name": "Product 1", "price": 19.99, "is_available": True},
        {"id": 2, "name": "Product 2", "price": 29.99, "is_available": False},
    ],
}


# Define the validation rules as a dictionary

validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "person",
                "products",
            ],
            "properties": {
                "person": {"bsonType": "object"},
                "required": [
                    "name",
                    "age",
                    "is_student",
                    "address",
                    "contacts",
                    "education",
                ],
                "properties": {
                    "name": {"bsonType": "string"},
                    "age": {"bsontype": "int"},
                    "is_student": {"bsonType": "bool"},
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
                    "contacts": {"bsonType": "array"},
                    "education": {"bsonType": "array"},
                },
                "products": {"bsonType": "array"},
            },
        },
    },
}
