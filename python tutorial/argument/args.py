# *args
# def total(a,b):
#     return a+b
# print(total(3,4))

# program1
# def all_total(*args):
#     print(args)
#     print(type(args))
# all_total(1,2,3,4,5,6,7,8)    

# program2
# def all_total(*args):
#     total=0
#     for num in args:
#         total=total+num
#     return total
# print(all_total(1,2,3,4))   

# *args with normal parameter program3
# def multiply_nums(*args):
#     multiply=1
#     for i in args:
#         multiply *= i
#     return multiply
# print(multiply_nums(1,2,3,4,5))    

# def multiply_nums(nums,*args):
#     multiply=1
#     print(nums)
#     for i in args:
#         multiply *= i
#     return multiply
# print(multiply_nums(1,2,3))    

# *args as argument program 4
def multiply_nums(*args):
    multiply=1
    print(args)
    for i in args:
        multiply*=i
    return multiply
nums=[]
print(multiply_nums(2,3))
