class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return self.first_name+" "+self.last_name

p1=Person('Harshit','Vashistha',23)
print(p1.full_name())