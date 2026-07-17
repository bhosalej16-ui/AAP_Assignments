from abc import ABC, abstractmethod

# ---------------- ABSTRACTION ----------------
class Person(ABC):

    @abstractmethod
    def display(self):
        pass


# ---------------- ENCAPSULATION ----------------
class Student(Person):

    def __init__(self, name, marks):
        self.name = name          # Public variable
        self.__marks = marks      # Private variable

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.__marks}")


# ---------------- INHERITANCE ----------------
class GraduateStudent(Student):

    def __init__(self, name, marks, course):
        super().__init__(name, marks)
        self.course = course

    # ---------------- POLYMORPHISM ----------------
    def display(self):
        print(f"Graduate Student : {self.name}")
        print(f"Course           : {self.course}")
        print(f"Marks            : {self.get_marks()}")


# ---------------- MAIN PROGRAM ----------------
s1 = Student("Jay", 85)
g1 = GraduateStudent("Rahul", 92, "Computer Science")

print("----- Student Details -----")
s1.display()

print("\nUpdating Marks...")
s1.set_marks(90)
print("Updated Marks:", s1.get_marks())

print("\n----- Graduate Student Details -----")
g1.display()