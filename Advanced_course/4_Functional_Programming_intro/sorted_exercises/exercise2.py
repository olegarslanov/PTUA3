# Write a Python program to sort a list of dictionaries buy color value using Lambda.
# Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

list = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

print(sorted(list, key=lambda x: x["color"]))

# print(list[0]["color"])
