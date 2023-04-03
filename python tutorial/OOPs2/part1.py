class Laptop:
    def __init__(self,brand,model_name,price):
        # instance variable
        self.brand=brand
        self.model_name=model_name
        self.price=price
    
    def applied_discount(self,number):
        # self.price
        off_price=(number/100)*self.price
        return self.price - off_price



#object of the class
laptop1=Laptop('hp','aullrtx',67000) 
print(laptop1.applied_discount(10))
laptop2=Laptop('apple','macbook',3000000)
print(laptop2.applied_discount(30))