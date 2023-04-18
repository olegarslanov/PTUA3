import json

data = """{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson" 
     } 
  ]   
}"""

data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))
# {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price'}, {'id': '02', 'name':
# 'Nick', 'lastname': 'Thameson'}]}

data_dict["student"][1]["name"] = "Kyle"
for student in data_dict["student"]:
    student.update({"gender": "male"})
print(data_dict)

# {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price', 'gender': 'male'},
# {'id': '02', 'name': 'Kyle', 'lastname': 'Thameson', 'gender': 'male'}]}
