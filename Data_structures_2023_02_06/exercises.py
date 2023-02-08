# Try creating structure like one here: link from an empty dictionary: my_dict = {}

info = {
	"name": "Albert",
	"surname": "Einstein",
	"occupation": {
		"role": "Professor",
		"workplace": {
            'adress':"Berlin",
            "University": "Galaktika"
        }
	},
    "languages": ["German", "Latin", "Italian", "English", "French"]
}

for language in info["languages"]:
    print(language)

