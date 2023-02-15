# 3.Given string: text = 'In this lecture we will review some additional functionalities 
# of python built-in data structures.' calculate how many words have letter 'e' in it.


sentense = 'In this lecture we will review some additional functionalities of python built-in data structures.'

count_letter=sentense.count("e")
print(f"'e' letter in sentence: {count_letter}")



#comprehension
# count_letter=[for all in text]
# print(f"'e' letter in sentence: {count_letter}")