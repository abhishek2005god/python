#Find Frequency of charachters in a string
name = input()
dict1 = {}
for i in name:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)    