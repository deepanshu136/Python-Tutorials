# here in this example we will create a sale in which all the laptop will goes in 10% discount and after the sale is over the discount price will retun to zero we will do this with the help of class variable
class Laptop:
    discount_percent=10
    def __init__(self,brand,model_name,price):
        # instance variable
        self.brand=brand
        self.model_name=model_name
        self.price=price
    
    def applied_discount(self):
        # self.price
        off_price=(self.discount_percent/100)*self.price
        return self.price - off_price



#object of the class
laptop1=Laptop('hp','aullrtx',67000) 
print(laptop1.applied_discount())
print(laptop1.__dict__)
laptop2=Laptop('apple','macbook',3000000)
laptop2.discount_percent=50
print(laptop2.applied_discount())
