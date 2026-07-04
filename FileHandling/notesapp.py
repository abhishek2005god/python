while True:
    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note Saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                print("\nYour Notes:")
                print(file.read())

        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")