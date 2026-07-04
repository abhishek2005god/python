#Print only vowel from the given string
text = "The quick brown fox jumps over the lazy dog"

for i in text:
    #check if i in this condition is vowel
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i,end=" ")