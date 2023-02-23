# Create a simple program that would log all inputs from the terminal. Configs 
# must show all additional data (time, date, level etc.)



import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG, filename='data.log',filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

name = input("Enter Your Name:")
logging.info(f"{name} has logged in successfully !!")

age = input("Your age:")
logging.debug(f"{name} has entered age {age}")


def add_few_number(a: int, b: int) -> int:
    logging.warning(f'Received numbers: a:{a} and b:{b}')
    
    return a + b

add_few_number(a=6, b=7)

