# updateing the instance of method which we have created previously
# Instance of method
import time
t1=time.time()
class Student:
    # constructor
    def __init__(self,roll_no,name,age):
        # instance variable
        self.roll_no=roll_no
        self.name=name
        self.age=age

    # instance method access instance variable
    def show(self):
        print('Roll number:',self.roll_no,'Name:',self.name, 'Age:',self.age)
    # instance method to modify instance variable
    def update(self,roll_number,age):
        self.roll_no=roll_number
        self.age=age
# create first object
print('First Student')
var=Student(20,"jessa",14)
# call instance method
var.show()
# modifying instance variable
print('Updated value of Roll_no. & Age')
var.update(30,15)
var.show()

# create second object
print('Second Student')
var1=Student(45,"kelly",16)
# call instance method
var1.show()
# modifying instance variable
print('Updated value of Roll_no. & Age')
var.update(23,45)
var.show()
t2=time.time()
print(t2-t1)
