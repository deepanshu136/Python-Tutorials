# make a program with decorator function  which will help us to calclate the time taken by the function to run

# import time
# t1=time.time()
# print('this is line one')
# x=5
# if x==5:
#     print('x is equal to 5')
# print("this is line two")
# l=[i for i in range(12) if i%2==0]
# print(l)
# print("this is line two")
# print("this is line two")
# print("this is line two")
# print("this is line two")
# print("this is line two")
# print("this is line two")
# t2=time.time()
# print(t2-t1)


# program 2
# from functools import wraps
# import time
# def calculate_time(function):
#     @wraps(function)
#     def wrapper_function(*args,**kwargs):
#         t1=time.time()
#         returned_value=function(*args,**kwargs)
#         t2=time.time()
#         total_time=t2-t1
#         print(f"this function took {total_time}")  
#         return returned_value
#     return wrapper_function
# @calculate_time
# def square_finder(n):
#     return [i**2 for i in  range(1,n+1)]

# square_finder(1000)



# program 3
from functools  import wraps
def only_int_allowed(function):
    @wraps(function)
    def wrapper_function(*args ,**kwargs):
        data_types=[]
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args,**kwargs)  
        else:
            print("Invalid argument")
    return wrapper_function          
@only_int_allowed
def add_all(*args):
    total=0
    for i in args:
        total+=i   
    return total
print(add_all(1,2,3,4,5))    