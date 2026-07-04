students = []

def add_student():
    student_id = input("Enter Student ID:")
    name = input("Enter Student name:")
    age = input("Enter Student age:")

    student = {
        "id": student_id,
        "name": name,
        "age": age
    }
    students.append(student)
    print("Student added successfully!")

def view_students():

    if len(students) == 0:
        print("No Students Found.")
        return

    print("\nStudent List\n")

    for student in students:
        print("----------------------")
        print("ID :", student["id"])
        print("Name :", student["name"])
        print("Age :", student["age"])

def search_student():
    search_id = input("Enter Student ID :")
    for student in students:
        if student["id"] == search_id:
            print("Student Found!")
            print(student)
        return
    print("Student Not Found!")

def delete_student():

    delete_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == delete_id:

            students.remove(student)

            print("Student Deleted!")

            return

    print("Student Not Found.")

def save_to_file():

    file = open("students.txt", "w")

    for student in students:

        line = student["id"] + "," + student["name"] + "," + student["age"] + "\n"

        file.write(line)

    file.close()

    print("Data Saved Successfully!")

def load_file():

    try:

        file = open("students.txt", "r")

        for line in file:

            data = line.strip().split(",")

            student = {
                "id": data[0],
                "name": data[1],
                "age": data[2]
            }

            students.append(student)

        file.close()

    except FileNotFoundError:
        pass


load_file()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        save_to_file()
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")