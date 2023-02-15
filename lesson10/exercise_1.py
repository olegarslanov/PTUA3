# Create at least 5 different functions by your own and test it.

#1
def print_smth():
    print('Hello world!')

print_smth()

#2
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#3
def my_function(f_name):
  print(f_name + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


#4
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


