# Create a function what would include full cycle of error handling
# (try/except/else/finally) with real world scenario example.

#1
def add_any (num_1:float,num_2:float)->float:
    
    try:
        result = num_1 + num_2
        return result       
    except TypeError as e:
        print(f'Error:{e}')
        result = None
    except Exception as e:
        print(f'Error:{e}')
        result = None
    finally:
        print(f"Answer: {result}")


add_any('a',1.25)



