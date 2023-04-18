# Palengvintas uzduoties variantas:
      
# Create a console program ,that at the start, asks to enter a sentence. 
# After that, it would show you 4 options to choose:

# 1) Make all letters in UpperCase
# 2) Count the letters
# 3) Print the longest word
# 4) exit.

# With every chosen option, print the result. (That means: lets say you choose
# option 3 - console prints longest word. Then, again console gives you the 
# option to choose until you choose option 4 to exit the program.)
    

print("It is program that ask to enter a sentence. You can choose make all letters in UpperCase, count the letters, or Print the longest word")    
  
sentence = input("Please input a sentence:")

print("Please choose option")


while True:

    print("1) Make all letters in UpperCase")
    print("2) Count the letters")
    print("3) Print the longest word")
    print("4) Exit")
 
    choice = input("Please enter Choice:")

    choise = choice.strip()   # choise priskiriam nauja input reiksme

    if (choice == "1"):
        sentence_upper = sentence.upper()
        print (sentence_upper)

    elif (choice == "2"):
        count_letters = len(sentence)
        print (count_letters)

    elif (choice == "3"):
        word_list = sentence.split()
        longest_word = max(word_list, key = len)
        print (longest_word)

    elif (choice == "4"):
        print("Program finish. Bye bye")
        break

    else:
        print("Wrong choice!")















