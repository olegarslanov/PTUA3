# dictionary

countries_and_capitals = {
    'Lithuania' : 'Vilnius',
    'Poland':'Warsaw',
    'Latvia':{
        'capital':'Riga',
        'population': '2000000'
    }
}

print (countries_and_capitals['Latvia']['capital'])

print(list(countries_and_capitals.items()))

print((countries_and_capitals.keys()))

print(list(countries_and_capitals.values()))

new_country = {'Spain':'Madrid', 'France':"Paris"}
countries_and_capitals.update(new_country)
print(countries_and_capitals)

# Add lists to dictionary
test_keys = ['Albert', 'Tom', 'Stephen']
test_values = [1,4,5]
my_dictionary = dict(zip(test_keys, test_values))
print(my_dictionary)

