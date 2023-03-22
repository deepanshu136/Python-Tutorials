# function returning function
# def outer_func():
#     def inner_func():
#         print("inside inner func")
#     return inner_func

# def outer_funce2(msg):
#     def inner_func2():
#         print(f"message is {msg}")
#     return inner_func2

# var=outer_funce2("hi there")    
# var()

# function returning function part 2
# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power
# cube =to_power(3)
# print(cube(5))

# square =to_power(2)
# print(square(4))

# decorator = enhance the  functionality of other function
# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is awsome function")
#         any_function()
#     return wrapper_function()    


# @decorator_function
# def func1():
#     print("this is function 1")
# def func2():
#     print("this is function 2")

# func2()

# new program
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''This is wrapper function'''
        print('this is awsome function')
        return any_function(*args,**kwargs)
    return wrapper_function   
@decorator_function
def func(a):
    print(f'This is function:{a}')
func(7)
@decorator_function
def add(c,d):
    '''This is add function'''
    return c+d
print(add(5,5))
help(add)
print(add.__doc__)


        

