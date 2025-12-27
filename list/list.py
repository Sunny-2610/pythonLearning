# Creating a list
students = ["Sunny", "Aman", "Rohit", "Neha"]

# Accessing elements
print("First student:", students[0])
print("Last student:", students[-1])

# Adding elements
students.append("Priya")
print("After adding a student:", students)

# Modifying an element
students[1] = "Amit"
print("After modifying:", students)

# Removing an element
students.remove("Rohit")
print("After removing Rohit:", students)

# Looping through the list
print("\nList of students:")
for name in students:
    print(name)

# List comprehension example
name_lengths = [len(name) for name in students]
print("\nLength of each name:", name_lengths)
