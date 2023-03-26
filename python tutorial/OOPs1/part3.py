# Instance of method
class Student:
    # constructor
    def __init__(self,name,age):
        # instance variable

        self.name=name
        self.age=age

    # instance method access instance variable
    def show(self):
        print('Name:',self.name, 'Age:',self.age)
    
# create first object
print('First Student')
var=Student("jessa",14)
# call instance method
var.show()

# create second object
print('Second Student')
var1=Student("kelly",16)
# call instance method
var1.show()
