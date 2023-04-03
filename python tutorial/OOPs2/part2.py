# class variable
class Circle:
    pi=3.14         # Class Vriable is defined here (The value of class variable is shared with  each object)so no need to create instace variable for pi and passing its valuer every time 
    def __init__(self,radius):
        self.radius=radius
        
    def calc_circumference(self):
        return 2*Circle.pi*self.radius

c=Circle(4)
c1=Circle(5)    
print(c.calc_circumference())    