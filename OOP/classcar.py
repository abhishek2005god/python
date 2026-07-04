# A class is like a blueprint (design plan)
# An object is a real thing made from that blueprint.

class Car:
    def __init__(self, brand, model, year):   #init is an constructor method that is called when an object is created and self is a reference to the current instance of the class
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print("----- Car Details -----")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def start_engine(self):
        print(self.brand, self.model, "engine started 🚗🔥")


# Creating objects
car1 = Car("Toyota", "Innova", 2020)
car2 = Car("BMW", "X5", 2023)

# Using methods
car1.show_info()
car1.start_engine()

print()

car2.show_info()
car2.start_engine()