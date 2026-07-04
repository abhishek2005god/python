class student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show_info(self):
        print("----- Student Details -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

    def is_passed(self):
        if self.marks > 40:
            print(self.name, "has passed the exam! 🎉")
        else:
            print(self.name, "has failed the exam. 😞")

# # Creating objects
# student1 = student("Abhishek", 20, 85)
# student2 = student("Krish", 19, 35)

# # Using methods
# student1.show_info()
# student1.is_passed()

# print()
# student2.show_info()
# student2.is_passed()

#OR TAKING INPUT FROM THE USER
name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = int(input("Enter student marks: "))

student1 = student(name, age, marks)  #Creating an object of the student class with user input

student1.show_info()
student1.is_passed()
