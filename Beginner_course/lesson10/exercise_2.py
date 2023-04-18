# Create a function that adds a string ending to each member in a list.


#1
def adding_str_to_list (list, string) -> str:
    my_new_list=[]

    for value in list:
        my_new_list.append(str(value)+str(string))

    return (my_new_list)

print(adding_str_to_list(['1','ada',';s@'],"da"))


#2
def add_string_to_list(list) -> str:
    for i in list:
        return list[0]+"s"+" "+list[1]+"s"+" "+list[2]+"s"

print(add_string_to_list(["Paulius", "Antanas", "Jonas"]))
