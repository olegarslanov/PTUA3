# Given the same string as in previous exercise: calculate count of letters that 
# have more than 5 characters.


sentence = 'In this lecture we will review some additional functionalities of python built-in data structures.'

# word_list = sentence.split()

new_word_list=[]

for word in sentence.split():
    if len(word)>5:
        new_word_list.append(word)

# new_word_str=''.join(new_word_list)

print(len(''.join(new_word_list)))


#comprehension



