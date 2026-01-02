class Student:
    # 1. Fixed name to __init__ and added proper spacing
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 2. Moved display() out of __init__ (same indentation level)
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# 3. Moved object creation outside of the class
s1 = Student("Sunny", 20)
s1.display()