from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        print(f"You are calling {function.__name__}")
        return function(*args,**kwargs)
    return wrapper_function

-@print_function_data
def add_function(a,b):
    '''This function takes two argument and returnm their sum'''
    return a+b

print(add_function(3,5))
print(add_function.__doc__) 
