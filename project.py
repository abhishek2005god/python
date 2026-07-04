# #Current age Calculator
# current_year= int(input("Enter Your Current Year : "))
# birth_year = int(input("Enter Your Birth Year : "))

# age = current_year - birth_year
# print("Your Age is :", age)


# #BMI Calculator
# weight = float(input("Enter Your Current Weight : "))
# height = float(input("Enter Your Current Height : "))

# bmi = weight/(height**2)
# print("Your bmi is : ", round (bmi,2))

# # Simple Caluclator
# num1 = float(input("Enter the number1 :"))
# num2 = float(input("Enter the number2 : "))

# print("Addition : ",num1 + num2)
# print("Subtraction : ",num1 - num2)
# print("Multiplication : ",num1 * num2)
# print("Division : ",num1 / num2)

# #Find Maximum in a List
# marks = [90,30,100,50,80,95]

# highest = marks[0]   #Iterative Approach
# for i in marks :
#     if i > highest:
#         highest = i
#         print(highest)

# #Grading System

# marks = int(input("Enter The Marks : "))
# if marks >= 90 and marks <=100 :
#     print("Grade A")
# elif marks >= 80 and marks <= 90 :
#     print("Grade B")
# elif marks >= 70 and marks <=80 :
#     print("Grade C")
# elif marks >= 60 and marks <=70 :
#     print("Grade D")
# elif marks < 60 :
#     print("E")
# else :
#     print("Invalid")

# #Square Pattern 
# for i in range (4):
#     for j in range (4):
#         print("#",end="")
#     print()

# #righttriangle pattern
# n = int(input())

# for i in range(1, n+1):
#     for j in range(i):
#         print("#", end=" ")
#     print()
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("#",end="")
    print()