x = 5
print(type(x)) #this will also tell the type which here it is class 
print (x) #<class 'int'>    5

#float 
f = 0.5
print(type(f))
print(f)

#Boolean  it is true or false
b = True
print(type(b))
print(b)

#Strings   textual data between " " or ' ' 
s1 = "My Name Is Abhishek *7297402"
print(type(s1))
print(s1)

#Power accepts two values base and power
c=5
d=3
print(c ** d)

#Nested Loop
age = int(input("Enter your age: "))

if age > 18:
    if age >= 65:
        print("Take Rest")
    else:
        print("You are Eligible")
        print("Drive Slow")
else:
    print("Wait till you turn 18")


#Print All Numbers From 1 to 10
i = 1
while i <= 10:
    print(i, end = " ")
    i += 1 #increments value by 1

#Print Sum OF All Numbers from 1 to 10
i = 1
add = 0
while i <= 10:
    add += i
    i += 1
print(add)