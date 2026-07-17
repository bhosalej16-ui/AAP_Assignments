class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # String Representation
    def __str__(self):
        return f"Student(Name: {self.name}, Marks: {self.marks})"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    # Length
    def __len__(self):
        return len(self.name)

    # Comparison Operators
    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

    # Arithmetic Operators
    def __add__(self, other):
        return self.marks + other.marks

    def __sub__(self, other):
        return self.marks - other.marks

    def __mul__(self, other):
        return self.marks * other.marks

    # Callable Object
    def __call__(self):
        print(f"{self.name} scored {self.marks} marks.")

    # Boolean Value
    def __bool__(self):
        return self.marks >= 40

    # Item Access
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "marks":
            return self.marks
        else:
            raise KeyError("Invalid Key")

    def __setitem__(self, key, value):
        if key == "name":
            self.name = value
        elif key == "marks":
            self.marks = value
        else:
            raise KeyError("Invalid Key")

    # Destructor
    def __del__(self):
        print(f"Object '{self.name}' is deleted.")


# ---------------- MAIN PROGRAM ----------------

s1 = Student("Jay", 85)
s2 = Student("Rahul", 75)

print("String (__str__):", s1)
print("Representation (__repr__):", repr(s1))

print("\nLength (__len__):", len(s1))

print("\nComparison Methods:")
print("s1 == s2 :", s1 == s2)
print("s1 > s2  :", s1 > s2)
print("s1 < s2  :", s1 < s2)

print("\nArithmetic Methods:")
print("s1 + s2 =", s1 + s2)
print("s1 - s2 =", s1 - s2)
print("s1 * s2 =", s1 * s2)

print("\nCallable (__call__):")
s1()

print("\nBoolean (__bool__):")
if s1:
    print(s1.name, "has passed.")
else:
    print(s1.name, "has failed.")

print("\nItem Access:")
print("Name :", s1["name"])
print("Marks:", s1["marks"])

s1["marks"] = 95
print("Updated Marks:", s1["marks"])