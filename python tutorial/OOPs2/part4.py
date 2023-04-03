class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance+=1
        self.first_name =first_name
        self.last_name=last_name
        self.age=age


p1=Person('Deepanshu','kumar',22)
p2=Person('Abhishek','Kumar',25)
p3=Person('Kailash','Ram',51)
print(Person.count_instance)

        