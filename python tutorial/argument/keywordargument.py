# keyword argument (kwargs)
# **kwargs (double star operator)
# kwargs as a parameter

# PROGRAM 1
def func(**kwargs):
    print(kwargs)

func(first_name='deepanshu', last_name='kumar')

# program 2 loops in dictionary
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
func(first_name='abhishek',last_name='kumar')        

# dictionary unpacking
def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
d={'name':'harshit', 'age':'22'}
func(**d)  

#  question for practice

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names =["abhishek" , "kumar"]
print(func(names, reverse_str=True))    

