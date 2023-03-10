# Create program that allows user to enter text
# Convert that text to Leet speak 1337
# print outcome


sentence = input("Please enter Your text:")

replacements = (('a','4'),('b','6'),('d','|>'),('e','3'),('o','0'),('s','5'),('t','7'),('i','1'),('n',"|\|"),('u','|_|'),('z','2'))

leet_sentence = sentence
for old,new in replacements:
    leet_sentence = leet_sentence.replace(old,new)


print(leet_sentence)

