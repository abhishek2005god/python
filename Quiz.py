quiz = {"What is the capital of Maharashtra?": "a",
         "What is the Language spoken in Maharashtra?": "b",
         "Who was the first Marathi litterateur to win the prestigious Jnanpith Award?": "a"}

options = {"What is the capital of Maharashtra?": ["a) Mumbai", "b) Pune", "c) Nagpur", "d) Nashik"],
            "What is the Language spoken in Maharashtra?": ["a) Hindi", "b) Marathi", "c) English", "d) Gujarati"],
            "Who was the first Marathi litterateur to win the prestigious Jnanpith Award?": ["a) V. S. Khandekar", "b) Vishnu Sakharam Khandekar", "c) Kusumagraj", "d) P. L. Deshpande"]}

score = 0

print("\nWelcome to the Maharashtra Quiz!\n")

for question in quiz:
    print(question)

    for option in options[question]:
        print(option)

    answer = input("Enter Your answer (a/b/c/d):").lower()

    if answer == quiz[question]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer!")

        print("\n The Quiz Is Finished! Thank you for participating in the quiz.")

print(f"\nYour final score is: {score}/{len(quiz)}")
