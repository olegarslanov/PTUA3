




query = {"budget": 100000}
fields = {"document_name": 1, "budget": 1}
document = document_manager.get_single_query(query, fields)
print(document)
