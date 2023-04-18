# Parašykite programą, kuri nuskaitys failo turinį ir performuos jį taip:
# {
#   "colors": [
#     {
#       "color": "black",
#       "rgb": "255, 255, 255",
#       "hex": "#000"
#     },
#     {
#       "color": "white",
#       "rgb": "0, 0, 0",
#       "hex": "#FFF"
#     }

import json


# {
#     "colors": [
#         {
#             "color": "black",
#             "category": "hue",
#             "type": "primary",
#             "code": {"rgba": [255, 255, 255, 1], "hex": "#000"},
#         },
#         {
#             "color": "white",
#             "category": "value",
#             "code": {"rgba": [0, 0, 0, 1], "hex": "#FFF"},
#         },
#         {
#             "color": "red",
#             "category": "hue",
#             "type": "primary",
#             "code": {"rgba": [255, 0, 0, 1], "hex": "#FF0"},
#         },
#         {
#             "color": "blue",
#             "category": "hue",
#             "type": "primary",
#             "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"},
#         },
#         {
#             "color": "yellow",
#             "category": "hue",
#             "type": "primary",
#             "code": {"rgba": [255, 255, 0, 1], "hex": "#FF0"},
#         },
#         {
#             "color": "green",
#             "category": "hue",
#             "type": "secondary",
#             "code": {"rgba": [0, 255, 0, 1], "hex": "#0F0"},
#         },
#     ]
# }

# Noredamas uzkrauti JSON objekta is failo:

with open(
    "https://github.com/robotautas/kursas/blob/master/requests/uzduotis.json", "r"
) as file:
    data = json.load(file)

print(data)
