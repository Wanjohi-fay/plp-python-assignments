# Base Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

# Inherited Class
class Smartwatch(Smartphone):  # Inherits from Smartphone
    def __init__(self, brand, model, storage, strap_type):
        super().__init__(brand, model, storage)
        self.strap_type = strap_type
    
    # Method Overriding (Polymorphism)
    def info(self):
        return f"{self.brand} {self.model} smartwatch with {self.strap_type} strap"

# Create Objects with your devices
phone = Smartphone("Tecno", "Spark 20", 128)
watch = Smartwatch("Oraimo", "Smartwatch", 8, "silicone")

# Output
print(phone.info())   # Tecno Spark 20 with 128GB storage
print(watch.info())   # Oraimo Smartwatch with silicone strap
phone.call("0712345678")
