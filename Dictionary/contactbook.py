#Print a Contact Book
contact={}
for i in range(3):
    name=input("Enter the name: ")
    phone=input("Enter the phone number: ")
    contact[name] = phone
print("\nContactBook :")

for name, phone in contact.items():
    print(name, ":", phone)