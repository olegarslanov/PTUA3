
def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y
 
def prod(x: int, y: int) -> int:
    return x * y
 
def div(x: int, y: int) -> int:
    return x // y

if __name__ == "__main__":
    print(f"I am in calc.py {__name__}")

# Uzrasas if __name__ == "__main__" kad duoti printuoti dali kodo, kuri yra po sio 
# uzraso tik esant sitame main lange (o ne kitame lange, kai mes importuojame 
# sita moduli i kita faila po uzrasu komandos nevykdys)