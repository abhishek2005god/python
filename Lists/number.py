numbers = []

for i in range(10):
    num = int(input(f"Enter The Number {i+1}: "))
    numbers.append(num)

print("\nAll Numbers Are:",numbers)
print("Higest Number Is:",max(numbers))
print("Lowest Number Is:",min(numbers))
print("Average Number Is:",sum(numbers)/len(numbers))
print("Total Numbers Are:",sum(numbers))
print("Sorted Numbers Are:",sorted(numbers))