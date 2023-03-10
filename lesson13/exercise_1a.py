# Create a simple calculus program as a script and as module.


#1 Create a simple calculus as a script

def add(x, y):
    return x + y

def sub(x, y):
    return x-y

def multi(x, y):
    return x*y

def div(x, y):
    if y == 0:
        raise ValueError ("Devide by 0 imposible")
    return x/y


if __name__ == "__main__":
    print("Please choice mathematical operation from list: \n1. Addition\n2. Substraction\n3. Multiplication\n4. Division")

    sign = input("Please choice mathematical operation number (1/2/3/4):")
    num1 = float(input("Please enter first number:"))
    num2 = float(input("Please enter second number:"))

    if sign == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif sign == '2':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif sign == '3':
        print(num1, "*", num2, "=", multi(num1, num2))
    elif sign == '4':
        try:
            print(num1, "/", num2, "=", div(num1, num2))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Invalid choice!")







