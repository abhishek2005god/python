marks = []

for i in range(5):
    mark = int(input(f"Enter Marks For Student {i+1}: "))
    marks.append(mark)

print("\nAll Marks Are:",marks)
print("Higest Marks Are:",max(marks))
print("Lowest Marks Are:",min(marks))
print("Average Marks Are:",sum(marks)/len(marks))
print("Total Marks Are:",sum(marks))
print("Sorted Marks Are:",sorted(marks))

#cd lists
#python studentmarksystem.py