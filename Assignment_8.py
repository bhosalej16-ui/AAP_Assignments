import os

path = os.path.dirname(os.path.abspath(__file__))

source = os.path.join(path, "input.txt")
destination = os.path.join(path, "output.txt")

with open(source, "r") as f:
    data = f.readlines()

count = len(data)
print("Total number of lines:", count)

print("\nFirst two lines:")
for i in range(min(2, count)):
    print(data[i].strip())

with open(destination, "w") as f:
    for i in range(min(2, count)):
        f.write(data[i])

print("\nFirst two lines copied successfully to output.txt")

#output
Total number of lines: 5

First two lines:
Hello, this is the first line.
This is the second line.

First two lines copied successfully to output.txt