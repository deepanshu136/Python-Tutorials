# Object Orientd Programming
class Person:
    def __init__(self,first_name,last_name,age):
        #initialize instance variable
        self.first_name =first_name
        self.last_name=last_name
        self.age=age
#creating object of the above defined class
p1=Person('Deepanshu','Kumar',22)
p2=Person('Abhishek','kumar',25)
#printing the object
print(p1.first_name)
print(p1.last_name)
print(p1.age)
print(p2.first_name)
print(p2.last_name)
print(p2.age)