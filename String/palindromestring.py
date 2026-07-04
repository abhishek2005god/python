#Check wheather the given string is palindrome or not
text = "racecar"

if text == text[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")