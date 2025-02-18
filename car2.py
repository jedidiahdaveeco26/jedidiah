class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Year: {self.year}")

# Create two car objects
car1 = Car("Lamborgini", "Aventador Ultimae", 2017)
car2 = Car("Nissan", "GTR R35", 2018)
car3 = Car("chevrolet", "Camaro V8", 2022)

# Display their details
car1.display_info()
print()  
car2.display_info()
print()  
car3.display_info()