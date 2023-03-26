class Laptop:
    def __init__(self,brand_name,model_name,price):
        # initializing instance variable
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name=brand_name+' '+model_name+' '+price
# creating the objects of above defined class
l1=Laptop('Dell','vostro',str(55000))
print(l1.laptop_name)
l2=Laptop('HP','pavellion',str(86000))
print(l2.laptop_name)
