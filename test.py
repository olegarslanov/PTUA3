import logging

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



# def add_few_number(a: int, b: int) -> int:
#     logging.warning(f"Received numbers: a:{a} and b:{b}")
#     return a + b

# add_few_number(a = 6, b = 7)


# def money_collected(amount: float) -> None:
#     logging.info(f"Amount of money received {amount}")
#     if amount == 0:
#         sum = amount + 1
#         logging.warning("Exepted amount larger than 0")
#     #doing smth else
#     else:
#         sum = amount + 2
#     return sum


# print(money_collected(0))

logging.basicConfig(level=logging.DEBUG, filename='data.log',filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# def money_collected(amount: float) -> float:
#     logging.info(f"Amount of money received {amount}")
#     if amount == 0:
#       logging.warning("Exepted amount, must be larger than 0")
#     #doing smth else

#     try:
#         # some code here
#         result = amount / amount
#         logging.debug(f'Result:{result}')
#         return result
    
#     except Exception as e:
#       logging.error(f'Error received: {e}')


# money_collected (0)



def emergency_stop(is_stop_event: bool) -> None:
   if is_stop_event:
      logging.critical(f'Had to stop device due to unexpected stop event')
      # func stop()

emergency_stop(True)

print(emergency_stop(True))