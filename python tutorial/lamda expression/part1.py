# lamda aexpression (As we know that in python Anonymus means a function without any name as we know that in in generally function is defined by def so the keyword lamda is helpful in defining in  anonymus function)
# This function accepts any count of inputs but only evaluates and returns one expression.
#  example no 1
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(int(input(""))))

# exapmle 2
# Code to demonstrate how we can use a lambda function  
calc=lambda num: num+10
print("Your added value is :" ,calc(int(input(""))))

# NOTE LAMBDA FUNCTION IS ONLY LIMITED TO THE SINGLE STATEMENT
# Python code to show the reciprocal of the given number to highlight the difference between def() and lambda

def reciprocal(num):
    return 1/num

lambda_reciprocal = lambda num : 1/num

print("defKeyword",reciprocal(6))
print("lambdaKeyword", lambda_reciprocal(6))

# Using lambada with the filter function
# filter function in python acccept two argument such as one os function and second is list
lista = [1,12,2,3,46,78,90,34,45,66]
odd_list=list(filter(lambda num: num %2 !=0, lista))
print(odd_list)

# lambada function with the map function in python
listb=[1,2,12,22,3,4,5,45]
squared_list =list(map(lambda num : num**2 , listb))
print(squared_list)

# labda function without if else
calc1 = lambda s : len(s) > 5
print(calc1("qwerta"))
