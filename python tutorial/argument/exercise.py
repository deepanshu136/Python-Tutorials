def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return("you did not pass any args")
    
num=[2,3,4]
print(to_power(4,*num))    