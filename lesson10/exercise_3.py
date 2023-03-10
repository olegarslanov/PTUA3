# Create a mini python program which would take two numbers as an input and 
# would return their sum, subtraction, division, multiplication.


#1
def aritmetic_with_two_numbers(num_1, num_2)->int:
   
    sum=num_1+num_2
    sub=num_1-num_2
    div=num_1/num_2
    multi=num_1*num_2
    print("Sum:",sum)
    print("Subtraction:",sub)
    print("Division:", div)
    print("Multiplication:", multi)

    return 

aritmetic_with_two_numbers(115,18)


#2
num_1,sign, num_2 = input("Please enter numbers and sign:").split(" ")
num_1=float(num_1)
num_2=float(num_2)


def calculator(num_1:float, sign:str, num_2:float)->float:
    user_input=num_1,sign,num_2
    if sign=="+":
        answer=num_1+num_2
    elif sign=="-":
        answer=num_1-num_2
    elif sign=="/":
        answer=num_1/num_2
    elif sign=="*":
        answer=num_1*num_2
    else:
        print("Something wrong with program")
    return(answer)

print("Answer is", calculator(num_1,sign,num_2))

#3
def find_subtraction(num_1, num_2=50, print_result=False):
    """Returns the sum of num_1 and num_2"""
    sub_nums=num_1-num_2
    if print_result:
        print(sub_nums)
    return sub_nums

find_subtraction(5,print_result=True)


#4
a= int(input("Add first integer:"))
b= int(input("Add second integer:"))

def add_two_numbers (a:int, b:int)-> tuple[int,int,float,int]:
    return a+b,a-b,a/b,a*b

print(add_two_numbers(a,b))
