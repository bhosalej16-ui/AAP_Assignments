import numpy as np

numbers = np.array(range(1, 11))

print("Array:", numbers)

print("First five numbers:", numbers[0:5])
print("Last five numbers:", numbers[-5:])
print("Numbers from index 2 to 6:", numbers[2:7])

total = numbers.sum()
average = numbers.mean()
largest = numbers.max()
smallest = numbers.min()

print("Total:", total)
print("Average:", average)
print("Largest value:", largest)
print("Smallest value:", smallest)

updated_numbers = numbers + 5

print("After adding 5 to each element:", updated_numbers)