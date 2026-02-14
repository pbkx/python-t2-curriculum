# A class is a blueprint for making objects (like real "things" in a code).
# Each object can store data (attributes) and do actions (methods).
class Student:
    # __init__ is the constructor. It runs automatically when you create a Student()
    # "self" means "this specific object" the student youre creating
    def __init__(self, name, grade):  # Save the student's name and grade as attributes on this object.
        self.name = name
        self.grade = grade

    def introduce(self):  # A method is a function that belongs to the class.
        print("Hi, my name is", self.name)
        print("I am in grade", self.grade)

# Create a Student object named student1
# This calls Student.__init__ automatically.
student1 = Student("Max", 11)
student1.introduce()  # Call methods on the object using dot notation.

student2 = Student("Ben", 10)
student2.introduce()

student2.grade = 12  # Change attributes with dot notation.
student2.introduce()

student2.name = "Benjamin"
student1.introduce()