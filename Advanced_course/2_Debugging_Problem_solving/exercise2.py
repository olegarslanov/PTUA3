# write a python script that adds all the numbers entered in the command line
# as arguments. Throw an error if user enters something other than number


import sys

file_name = sys.argv[0]
greeting = f"{sys.argv[1]} {sys.argv[2]}"


print(f"{greeting} from {file_name}")
