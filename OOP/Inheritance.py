# class Employee:
#     def __init__(self, name, Salary):
#         self.name = name
#         self.salary = Salary

#     def display(self):
#         print(self.name)
#         print(self.salary)

# class Manager(Employee):

#     def manage(self):
#         print("Managing the team")

# manager1 = Manager("Abhishek", 50000)

# manager1.display()
# manager1.manage()

# #2
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# dog1 = Dog()
# dog1.sound()
# dog1.bark()

#3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("\nEMPLOYEE DETAILS:")
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def manage(self):
        print(self.name," is managing the team.")

class Developer(Employee):
    def develop(self):
        print(self.name," is developing the software.")

manager = Manager("Abhishek", 50000)
developer = Developer('Rohit', 40000)

manager.display()
manager.manage()

developer.display()
developer.develop()