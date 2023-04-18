# third, basic tasks with numbers

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
    print(f"It is number module!")