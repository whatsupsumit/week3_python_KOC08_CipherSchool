class Laptop:
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name


laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name)
