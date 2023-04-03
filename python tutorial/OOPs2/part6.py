# CLASS METHOD AS A CONSTRUCTOR
class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        # instance variable
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
 
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__} class."
     
    # instance method 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18
     
# class object
p1=Person('deepanshu','kumar',22)
p2=Person('Yukta','kumari',8)