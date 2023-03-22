# this is decorator
# def print_args(func):
#     def inner_func(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         return func(*args, **kwargs)
#     return inner_func
# @print_args
# def multiply(num_a, num_b):
#     return num_a*num_b
# print(multiply(3,5))
# help(print_args)
# help(multiply) 

# program 2
# def square(a):
#     return a**2
# print(square(2))

def square(a):
    return a**2 
l=[1,3,5,7]
# print(list(map(square,l)))

def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(square,l) )