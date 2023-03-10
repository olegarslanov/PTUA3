# You are given an input array of bigrams, and an array of words. Write a function
# that returns True if every single bigram from this array can be found at least once
# in an array of words.

# Example:
# can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
# can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
# can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False




tuple_list = (["at", "be", "th", "au"], ["beautiful", "the", "hat"])

def check_leters_in_words(tuple_list): 
    list_bool =[]
    while True:
        for word in tuple_list[1]:
            for letter in tuple_list[0]:
                if letter in word:
                    list_bool.append(True)
        break
    if len(set(list_bool)) == 1:
        print(True)         
    else:
        print(False)
    
check_leters_in_words(tuple_list)